from happyhour.models import Favorites
from django.shortcuts import render
from django.views.generic import View

class FavoritesView(View):
	template_name = "happyhour/favorite_list.html"
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			user = request.user
			favorites = Favorites.objects.filter(user=user.id).order_by("-restaurant__rating")
			return render(request, self.template_name, {'favorites': favorites,
														'user': user})
