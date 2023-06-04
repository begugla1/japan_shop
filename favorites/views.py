from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView

from .favorites import Favorites


@login_required(login_url='login')
def add_favorite(request, product_id):
    favorites = Favorites(request)
    favorites.add(request, product_id)
    return redirect(request.META.get('HTTP_REFERER'))


def delete_favorite(request, product_id):
    favorites = Favorites(request)
    favorites.delete(request, product_id)
    return redirect(request.META.get('HTTP_REFERER'))


def clear_favorites(request):
    favorites = Favorites(request)
    favorites.clear(request)
    return redirect(request.META.get('HTTP_REFERER'))


class FavoritesShow(LoginRequiredMixin, TemplateView):
    template_name = 'favorites/show_favs.html'
    login_url = 'login'
