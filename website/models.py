"""Import line."""
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
    count = models.IntegerField()
    id_in_arr = models.IntegerField()


class Trade(models.Model):
    """Class line."""
    action = models.TextField()
    id_nft = models.IntegerField()
    price_array = models.IntegerField()
    chat = models.TextField()
    owner = models.TextField()
    new_owner = models.TextField()
    time = models.TextField()


class NFTPACK(models.Model):
    """Class line."""
    name = models.TextField()
    price_array = ArrayField(models.IntegerField())
