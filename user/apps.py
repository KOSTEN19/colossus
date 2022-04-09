"""Import line"""
from django.apps import AppConfig


class UserConfig(AppConfig):
    """Class line"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'
    verbose_name = 'Users'
    label = 'users'
