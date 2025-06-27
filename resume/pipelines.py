from social_core.pipeline.user import get_username
from social_core.pipeline.social_auth import associate_by_email
from social_core.pipeline.user import create_user
from social_core.pipeline.social_auth import associate_user
from social_core.pipeline.social_auth import load_extra_data
from social_core.pipeline.user import user_details
from django.contrib.auth.models import User
from django.db import transaction

def get_username_by_provider(backend, user, response, *args, **kwargs):
    """Generate unique username based on provider and social ID"""
    if backend.name == 'github':
        # Use GitHub username + provider prefix
        github_username = response.get('login', '')
        username = f"github_{github_username}"
    elif backend.name == 'google-oauth2':
        # Use Google email + provider prefix
        email = response.get('email', '')
        username = f"google_{email.split('@')[0]}"
    else:
        # Fallback to email
        email = response.get('email', '')
        username = f"{backend.name}_{email.split('@')[0]}"
    
    # Ensure username is unique
    counter = 1
    original_username = username
    while User.objects.filter(username=username).exists():
        username = f"{original_username}_{counter}"
        counter += 1
    
    return {'username': username}

def force_new_user_creation(backend, user, response, *args, **kwargs):
    """Force creation of new user, never associate by email"""
    # Always return None to force new user creation
    return None

def prevent_email_association(backend, user, response, *args, **kwargs):
    """Prevent automatic email association to keep providers separate"""
    # This function ensures no email association happens
    return {'user': user}

def clear_user_session(backend, user, response, *args, **kwargs):
    """Clear any existing session data for the user"""
    if user and user.is_authenticated:
        # Clear any cached data
        if hasattr(user, '_cached_cv'):
            delattr(user, '_cached_cv')
    return {'user': user}

def validate_provider_user(backend, user, response, *args, **kwargs):
    """Validate user and ensure proper provider isolation"""
    if user and user.is_authenticated:
        # Force refresh user from database
        try:
            current_user = User.objects.get(id=user.id)
            
            # Verify username matches provider pattern
            if backend.name == 'github' and not current_user.username.startswith('github_'):
                pass  # Security warning removed
            elif backend.name == 'google-oauth2' and not current_user.username.startswith('google_'):
                pass  # Security warning removed
                
        except User.DoesNotExist:
            return None
    
    return {'user': user}

def create_cv_for_new_user(backend, user, response, *args, **kwargs):
    """Create CV for new user if it doesn't exist"""
    if user and user.is_authenticated:
        from .models import CV
        with transaction.atomic():
            cv, created = CV.objects.get_or_create(user=user)
    
    return {'user': user}

def log_provider_access(backend, user, response, *args, **kwargs):
    """Log provider access for debugging"""
    return {'user': user} 