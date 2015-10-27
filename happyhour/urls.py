from django.conf.urls import url
from happyhour import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^v1/restaurants/$', views.RestaurantList.as_view()),
    url(r'^v1/restaurants/(?P<pk>[0-9]+)/$', views.RestaurantDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)