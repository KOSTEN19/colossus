"""Import line."""
import chardet
from django.core.exceptions import ValidationError
from django.core.validators import validate_image_file_extension
from PIL import Image
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
    in_market = models.TextField()
    count =  models.IntegerField()
    id_in_arr = models.IntegerField()

class Trade(models.Model):
    action = models.TextField()
    id_nft =  models.IntegerField()
    price_array  = models.IntegerField()
    chat  = models.TextField()
    owner = models.TextField()
    new_owner = models.TextField()
    time = models.TextField()
class NFTPACK (models.Model):
    name = models.TextField()
    price_array = ArrayField(models.IntegerField())
    #chat = ArrayField(models.CharField(max_length=200), blank=True)
     
