from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200,null=True)
    phone_number = models.CharField(max_length=20,null=True)
    rating = models.DecimalField(null=True, decimal_places=1, max_digits=5)
    location_lat = models.FloatField(null=True)
    location_long = models.FloatField(null=True)
    image_url = models.URLField(max_length=200, null=True)
