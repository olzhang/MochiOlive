from happyhour.models import Restaurant, Favorites
from django.shortcuts import render
from django.views.generic.list import ListView
from django.shortcuts import render
from django.views.generic import View

# class RestaurantPage(ListView):
# 	queryset=Restaurant.objects.order_by("-rating")
# 	model = Restaurant
#
# 	def get_context_data(self, **kwargs):
# 	    """
# 	    gets information about all happy hour restaurants and sends to template for display.
# 	    """
# 	    context = super(RestaurantPage, self).get_context_data(**kwargs)
# 	    return context

class RestaurantView(View):
	template_name = "happyhour/restaurant_list.html"
	def get(self, request, *args, **kwargs):
		restaurants = Restaurant.objects.order_by("-rating")
		if request.user.is_authenticated():
			user = request.user
			print user.id
			print "authenticated"
			favorites = Favorites.objects.filter(user=user.id)
			print favorites
			return render(request, self.template_name, {'restaurants': restaurants,
														'user': user,
														'favorites': favorites})
		return render(request, self.template_name, {'restaurants': restaurants})
