from rest_framework import serializers
from happyhour.models import Restaurant, Favorites

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address', 'phone_number', 'rating', 'location_lat', 'location_long', 'image_url')

class FavoriteSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Favorites 
		fields = ('id', 'user', 'restaurant')