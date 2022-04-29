"""Import line."""
import chardet
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import ArrayField
from django.db import models


class NFT(models.Model):
    """Class line."""
    objects = models.Manager()
    image = models.ImageField(null=True, upload_to='static/nft/nft_pack/')
    name = models.TextField()
    price = models.IntegerField()
    description = models.TextField()
    owner = models.TextField()

class Trade(models.Model):
    id_nft =  models.IntegerField()
    price_array  = models.IntegerField()
    chat  = models.TextField()
    owner = models.TextField()
    new_owner = models.TextField()
    
    #price_array = ArrayField(models.IntegerField())
    #chat = ArrayField(models.CharField(max_length=200), blank=True)
     
