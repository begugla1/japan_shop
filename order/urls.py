from django.urls import path, include

from . import views


urlpatterns = [
    path('create', views.OrderCreate.as_view(), name='order_create'),
    path('show', views.OrderShow.as_view(), name='order_show'),
    path('clear/<int:order_id>', views.order_delete, name='order_clear'),
    path('clear_all', views.order_delete_all, name='order_clear_all')
]
