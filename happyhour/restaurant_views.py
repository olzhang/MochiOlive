from happyhour.models import Restaurant
from django.shortcuts import render


def restaurant_list(request):
    """
    gets information about all happy hour restaurants and sends to template for display.
    """
    restaurants = Restaurant.objects.order_by('-rating')
    return render(request, 'happyhour/restaurant_base.html', {'restaurants': restaurants})