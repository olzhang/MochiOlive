from happyhour.models import Restaurant
from django.shortcuts import render
from django.db.models import Q


def restaurant_filter(request):
    """
    delete any invalid data entries- no name or no address. 
    """
    restaurants = Restaurant.objects.filter(Q(name__isnull=True) | Q(address__isnull=True)).delete()
    return render(request, 'happyhour/restaurant_base.html', {'restaurants': restaurants})