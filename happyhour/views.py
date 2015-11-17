from django.shortcuts import render
from happyhour.models import Restaurant
from happyhour.serializers import RestaurantSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class RestaurantList(APIView):
    """
    GET: list all restaurants
    POST: add a new restaurant
    """
    def get(self, request, format=None):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            restaurants = Restaurant.objects.filter(name=request.data['name'],
                                                    address=request.data['address'],
                                                    phone_number=request.data['phone_number'],
                                                    rating=request.data['rating'],
                                                    location_lat=request.data['location_lat'],
                                                    location_long=request.data['location_long'],
                                                    image_url=request.data['image_url'])
            if not restaurants.exists():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RestaurantDetail(APIView):
    """
    GET: get specific restaurant based on id
    PUT: update specific restaurant based on id
    DELETE: delete a restaurant specified by id
    """
    def get_object(self, pk):
        try:
            return Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        restaurant = self.get_object(pk)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        restaurant = self.get_object(pk)
        serializer = RestaurantSerializer(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        restaurant = self.get_object(pk)
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserFavoritesList(APIView):
    """
    GET: list all favorite restaurants of a user
    POST: add a new favorite restaurant to a user
    """
    def get_object(self, user):
        try: 
            return Favorites.objects.get(user=user)
        except Favorite.DoesNotExist:
            raise Http404

    def get(self, request, user, format=None): 
        favorites = self.get_object(user)
        serializer = FavoriteSerializer(favorites)
        return Response(serializer.data)

    def post(self, request, user, format=None):
        serializer = FavoriteSerializer(data=request.data)
        if serializer.is_valid:
            favorites = Favorites.objects.filter(name=user, 
                address=request.data['restaurant'],
                phone_number=request.data['twitter'])
            if not favorites.exists():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






