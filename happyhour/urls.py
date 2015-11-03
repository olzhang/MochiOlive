from django.conf.urls import url
from happyhour import views, restaurant_views, restaurant_admin
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^v1/restaurants/$', views.RestaurantList.as_view()),
    url(r'^v1/restaurants/(?P<pk>[0-9]+)/$', views.RestaurantDetail.as_view()),
    url(r'^happy-hour-restaurants/$', restaurant_views.restaurant_list, name='restaurant_list'),
    url(r'^happy-hour-restaurants/filter/$', restaurant_admin.restaurant_filter)

]

urlpatterns = format_suffix_patterns(urlpatterns)