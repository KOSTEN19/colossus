from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class NFT(models.Model):
    image = models.ImageField(upload_to='NFT_base_folder/')
    name = models.TextField()
    price = models.IntegerField()
    description = models.TextField()
    owner = models.TextField()
# class CustomUser(AbstractBaseUser):
 #   USERNAME_FIELD  = models.CharField()
 #  PASSWORD_FIELD = models.CharField()
    # not USERNAME_FIELD = username

 #   balance = models.IntegerField()


"""
class CustomUser(AbstractBaseUser):
    USERNAME_FIELD  = models.CharField()
    PASSWORD_FIELD = models.CharField()
    not USERNAME_FIELD = username
    balance = models.IntegerField()
"""
