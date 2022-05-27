"""Import line"""
from django.db import models
from django.contrib.auth.models import AbstractUser


def default_thing():
    """Function line"""
    return []


class CustomUser(AbstractUser):
    """Class line"""
    profile_pic = models.ImageField(null=True, blank = True , upload_to = 'static/users/pictures', default='/static/wllp/7.png')
    balance = models.IntegerField(default=100)
    spend_total = models.IntegerField(default=0)
    nft_buyght = models.IntegerField(default=0)
    nft_sell = models.IntegerField(default=0)
