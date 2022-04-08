"""Import line"""
from distutils.command.upload import upload
from django.db import models

class NFT(models.Model):
    """Class line"""
    objects = models.Manager()
    image = models.ImageField(null = True, upload_to = 'static/nft/nft_pack/')
    name = models.TextField()
    price = models.IntegerField()
    description = models.TextField()
    owner = models.TextField()
