"""Import line"""
from django.db import models
from django.contrib.auth.models import AbstractUser


def default_thing():
    """Function line"""
    return []


class CustomUser(AbstractUser):
    """Class line"""
    profile_pic = models.ImageField(null=True, blank = True , upload_to = 'static/users/pictures', default='/static/wllp/7.png')
    balance = models.IntegerField(default=100000)
