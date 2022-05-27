"""Import line."""
from django.contrib.postgres.fields import ArrayField
from django.db import models


class NFT(models.Model):
    """Class line."""

    image = models.ImageField(null=True, upload_to='static/nft/nft_pack/')
    name = models.TextField()
    price = models.IntegerField()
    author = models.TextField()
    description = models.TextField()
    owner = models.TextField()
    count = models.IntegerField()
    in_market = models.BooleanField()
    id_in_arr = models.IntegerField()



class Trade_sell(models.Model):
    """Class line."""
    id_nft = models.IntegerField()
    new_price = models.IntegerField()
    time = models.TextField()
    image = models.ImageField(null=True, upload_to='static/nft/nft_pack/')
    name = models.TextField()
    price = models.IntegerField()
    author = models.TextField()
    description = models.TextField()
    owner = models.TextField()
    owner_image =  models.ImageField(null=True, blank = True , upload_to = 'static/users/pictures', default='/static/wllp/7.png')
    count = models.IntegerField()
    in_market = models.BooleanField()
    id_in_arr = models.IntegerField()

class Trade_buy(models.Model):
    id_nft = models.IntegerField()
    new_price = models.IntegerField()
    time = models.TextField()
    author = models.TextField()
    message =  models.TextField()
class NFTPACK(models.Model):
    """Class line."""
    name = models.TextField()
    price_array = ArrayField(models.IntegerField())
