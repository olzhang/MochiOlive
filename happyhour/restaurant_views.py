from happyhour.models import Restaurant, Favorites
from django.shortcuts import render
from django.views.generic import View

class RestaurantView(View):
	template_name = "happyhour/restaurant_list.html"
	def get(self, request, *args, **kwargs):
		restaurants = Restaurant.objects.order_by("-rating")
		if request.user.is_authenticated():
			user = request.user
			favorites = Favorites.objects.filter(user=user.id)
			return render(request, self.template_name, {'restaurants': restaurants,
														'user': user,
														'favorites': favorites})
		return render(request, self.template_name, {'restaurants': restaurants})
