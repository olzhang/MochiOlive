from happyhour.models import Restaurant
from django.shortcuts import render
from django.views.generic.list import ListView

class RestaurantPage(ListView):
	queryset=Restaurant.objects.order_by("-rating")
	model = Restaurant

	def get_context_data(self, **kwargs):
	    """
	    gets information about all happy hour restaurants and sends to template for display.
	    """
	    context = super(RestaurantPage, self).get_context_data(**kwargs)
	    return context
