from django.core.exceptions import ValidationError
from django.core.validators import validate_email as django_validate_email
from django.contrib.auth import get_user_model
import re
# from .models import UserProfile


User = get_user_model()


def validate_email(email):
    try:
        # Validate email format using Django's validate_email
        django_validate_email(email)
    except ValidationError:
        raise ValidationError({'email': ['Invalid email address']})

    if User.objects.filter(email=email).exists():
        raise ValidationError({'email': ['Email is already in use']})


def validate_username(username):
    pattern = r'^[a-zA-Z0-9]+$'

    # Check if the username matches the pattern
    if not re.match(pattern, username):
        raise ValidationError(
            {'username': ['Username can only contain letters and numbers']})

    if User.objects.filter(username=username).exists():
        raise ValidationError({'username': ['Username is already taken']})


def validate_password(password):
    if len(password) < 6:
        raise ValidationError(
            {'password': ['Password must be at least 6 characters long']})

    # Regular expression pattern to require at least one letter, one number, and one special character
    pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$'

    if not re.match(pattern, password):
        raise ValidationError({'password': [
                              'Password must contain at least one letter, one number, and one special character']})


# def profile_exists_for_user(user):
#     """
#     Check if a profile already exists for the given user.
#     """
#     return UserProfile.objects.filter(user=user).exists()