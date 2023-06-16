from django.urls import path

from . import views


urlpatterns = [
    path('', views.CartDetail.as_view(), name='cart_detail'),
    path('add/<int:product_id>', views.cart_add, name='cart_add'),
    path('delete/<int:product_id>', views.cart_remove, name='cart_delete'),
    path('clear', views.cart_clear, name='clear'),
]
