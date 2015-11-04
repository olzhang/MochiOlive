from django.conf.urls import url
from happyhour import views, restaurant_views, admin_view
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^v1/restaurants/$', views.RestaurantList.as_view()),
    url(r'^v1/restaurants/(?P<pk>[0-9]+)/$', views.RestaurantDetail.as_view()),
    url(r'^happy-hour-restaurants/$', restaurant_views.restaurant_list, name='restaurant_list'),
    url(r'^login/admin/$', 'django.contrib.auth.views.login', {'template_name': 'happyhour/login.html'}),
    url(r'^admin/dashboard/$', admin_view.restaurant_list_admin, name='restaurant_list_admin'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/happy-hour-restaurants/'})
]

urlpatterns = format_suffix_patterns(urlpatterns)