from happyhour.models import Restaurant
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/admin/")
def restaurant_list_admin(request):
    """
    gets information about all happy hour restaurants and sends to template for display.
    """

    restaurants = Restaurant.objects.order_by('-rating')
    return render(request, 'happyhour/admin_base.html', {'restaurants': restaurants})
