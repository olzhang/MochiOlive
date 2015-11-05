from happyhour.models import Restaurant
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic.list import ListView
from yelp_client import YelpClient
import yelp_client
from django.shortcuts import redirect

class RestaurantAdmin(ListView):
	queryset = Restaurant.objects.order_by('-rating')
	model = Restaurant 
	template_name = "happyhour/admin_base.html"
	
	def get_context_data(self, **kwargs):
		"""
		gets information about all happy hour restaurants and sends to template for display.
		"""
		context = super(RestaurantAdmin, self).get_context_data(**kwargs)
		return context

class RestaurantFilter(ListView):
	queryset = Restaurant.objects.filter(Q(name__isnull=True) | Q(address__isnull=True))
	model = Restaurant 
	template_name = "happyhour/filter_base.html"

	def get_context_data(self, **kwargs):
		"""
		gets information about all happy hour restaurants and sends to template for display.
		"""
		context = super(RestaurantFilter, self).get_context_data(**kwargs)
		self.queryset.delete()
		return context

class RestaurantUpdate(ListView):
	model = Restaurant
	template_name = "happyhour/update_base.html"

	def get_context_data(self, **kwargs):
		"""
		updates the restaurant information
		"""
		client = YelpClient()
		data = client.get_all_sets(yelp_client.keys, 200)
		post_yelp = yelp_client.TranslatePostYelp()
		post_yelp.post_all_to_database(data)
		context = super(RestaurantUpdate, self).get_context_data(**kwargs)
		return context