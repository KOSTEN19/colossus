from urllib import request
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
   # USERNAME_FIELD  = 
   #PASSWORD_FIELD = models.CharField()
    balance = models.IntegerField(default=100000)