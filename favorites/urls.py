from django.urls import path
from . import views


urlpatterns = [
    path('add/<int:product_id>', views.add_favorite, name='add_fav'),
    path('delete/<int:product_id>', views.delete_favorite, name='delete_fav'),
    path('clear', views.clear_favorites, name='clear_favs'),
    path('show', views.FavoritesShow.as_view(), name='show_favs')
]
