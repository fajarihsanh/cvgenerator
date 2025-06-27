from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import transaction
from resume.models import CV

class Command(BaseCommand):
    help = 'Clear existing social auth associations and force provider separation'

    def handle(self, *args, **options):
        self.stdout.write('Starting social auth cleanup...')
        
        with transaction.atomic():
            try:
                from social_django.models import UserSocialAuth
                
                # Get all social auth records
                social_auths = UserSocialAuth.objects.all()
                self.stdout.write(f'Found {social_auths.count()} social auth records')
                
                # Group by email to find conflicts
                email_groups = {}
                for sa in social_auths:
                    email = sa.user.email
                    if email not in email_groups:
                        email_groups[email] = []
                    email_groups[email].append(sa)
                
                # Process each email group
                for email, auths in email_groups.items():
                    if len(auths) > 1:
                        self.stdout.write(f'Found {len(auths)} providers for email: {email}')
                        
                        # Keep only the first one, delete others
                        for i, auth in enumerate(auths[1:], 1):
                            self.stdout.write(f'  Deleting duplicate: {auth.provider} -> {auth.user.username}')
                            auth.delete()
                
                # Now fix usernames for remaining users
                users = User.objects.all()
                for user in users:
                    self.stdout.write(f'Processing user: {user.username} (ID: {user.id})')
                    
                    # Check if user already has provider prefix
                    if user.username.startswith(('github_', 'google_')):
                        self.stdout.write(f'  User {user.username} already has provider prefix - skipping')
                        continue
                    
                    # Get social auth for this user
                    try:
                        social_auth = UserSocialAuth.objects.get(user=user)
                        provider = social_auth.provider
                        
                        if provider == 'github':
                            new_username = f"github_{user.username}"
                        elif provider == 'google-oauth2':
                            new_username = f"google_{user.username}"
                        else:
                            new_username = f"{provider}_{user.username}"
                        
                        # Ensure username is unique
                        counter = 1
                        original_username = new_username
                        while User.objects.filter(username=new_username).exists():
                            new_username = f"{original_username}_{counter}"
                            counter += 1
                        
                        # Update username
                        old_username = user.username
                        user.username = new_username
                        user.save()
                        
                        self.stdout.write(f'  Updated {old_username} -> {new_username} (Provider: {provider})')
                        
                    except UserSocialAuth.DoesNotExist:
                        self.stdout.write(f'  User {user.username} has no social auth - skipping')
                    except Exception as e:
                        self.stdout.write(f'  Error processing {user.username}: {e}')
                
            except ImportError:
                self.stdout.write('social_django not installed')
            except Exception as e:
                self.stdout.write(f'Error: {e}')
        
        self.stdout.write(self.style.SUCCESS('Social auth cleanup completed!')) 