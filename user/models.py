"""Import line"""

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """Class line"""
    #USERNAME_FIELD =
    #PASSWORD_FIELD = models.CharField()
    profile_pic = models.ImageField(null=True, blank = True , upload_to = 'static/users/pictures')
    balance = models.IntegerField(default=100000)
