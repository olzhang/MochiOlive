from django.conf.urls import url
from happyhour import views, restaurant_views, admin_view
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^v1/restaurants/$', views.RestaurantList.as_view()),
    url(r'^v1/restaurants/(?P<pk>[0-9]+)/$', views.RestaurantDetail.as_view()),
    url(r'^v1/favorites/user/(?P<user>[0-9]+)/$', views.UserFavoritesList.as_view()),
    url(r'^v1/favorites/twitter/(?P<twitter>[0-9]+)/$', views.UserFavoritesList.as_view()),
    url(r'^$', TemplateView.as_view(template_name='homepage_base.html')),
    url(r'^login/user/$', TemplateView.as_view(template_name='happyhour/signup_login.html')),
    url(r'^happy-hour-restaurants/$', restaurant_views.RestaurantView.as_view()),
    url(r'^happy-hour-restaurants/login/admin$', 'django.contrib.auth.views.login', {'template_name': 'happyhour/login.html'}),
    url(r'^login/admin/$', 'django.contrib.auth.views.login', {'template_name': 'happyhour/login.html'}),
    url(r'^admin/dashboard/$', login_required(admin_view.RestaurantAdmin.as_view()), name='restaurant_list_admin'),
    url(r'^admin/dashboard/filter/$', admin_view.RestaurantFilter.as_view()),
    url(r'^admin/dashboard/update/$', admin_view.RestaurantUpdate.as_view()),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/happy-hour-restaurants/'})
]


urlpatterns = format_suffix_patterns(urlpatterns)


