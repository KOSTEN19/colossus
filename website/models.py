"""Import line"""
from django.db import models

class NFT(models.Model):
    """Class line"""
    objects = models.Manager()
    image = models.ImageField(upload_to='NFT_base_folder/')
    name = models.TextField()
    price = models.IntegerField()
    description = models.TextField()
    owner = models.TextField()
