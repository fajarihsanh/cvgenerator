from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import transaction
from resume.models import CV

class Command(BaseCommand):
    help = 'Fix existing users to separate them by OAuth provider'

    def handle(self, *args, **options):
        self.stdout.write('Starting user provider separation...')
        
        with transaction.atomic():
            # Get all users
            users = User.objects.all()
            
            for user in users:
                self.stdout.write(f'Processing user: {user.username} (ID: {user.id})')
                
                # Check if user already has provider prefix
                if user.username.startswith(('github_', 'google_')):
                    self.stdout.write(f'  User {user.username} already has provider prefix - skipping')
                    continue
                
                # Try to determine provider from social auth
                try:
                    from social_django.models import UserSocialAuth
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
        
        self.stdout.write(self.style.SUCCESS('User provider separation completed!')) 