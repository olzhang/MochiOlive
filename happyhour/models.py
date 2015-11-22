from django.db import models
from django.contrib.auth.models import User

from allauth.account.signals import user_logged_in
from django.dispatch import receiver
from django.contrib import messages

class Restaurant(models.Model):
    name = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200,null=True)
    phone_number = models.CharField(max_length=20,null=True)
    rating = models.DecimalField(null=True, decimal_places=1, max_digits=5)
    location_lat = models.FloatField(null=True)
    location_long = models.FloatField(null=True)
    image_url = models.URLField(max_length=200, null=True)

class Favorites(models.Model):
	user = models.ForeignKey(User)
	restaurant = models.ForeignKey(Restaurant)

@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    messages.success(request, ("Thank you for signing in with twitter account %(username)s") % {'username': user.username},)