from django.db import models

class Restaurant(models.Model):
    name  = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200,null=True)
    phone_number = models.CharField(max_length=20,null=True)
    rating  = models.IntegerField(null=True)
    lat = models.FloatField(null=True)
    long = models.FloatField(null=True)
    image_url = models.URLField(max_length=200, null=True)
