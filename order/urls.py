from django.urls import path, include

from . import views


urlpatterns = [
    path('create', views.OrderCreate.as_view(), name='order_create'),
    path('success', views.OrderSuccess.as_view(), name='order_success'),
    path('show', views.OrderShow.as_view(), name='order_show'),
    path('payment/<int:order_id>', views.order_pay, name='order_payment'),
    path('clear/<int:order_id>', views.order_delete, name='order_clear'),
]
