from django.urls import path, include

from . import views


urlpatterns = [
    path('create', views.OrderCreate.as_view(), name='order_create'),
    path('success', views.OrderSuccess.as_view(), name='order_success'),
    path('show', views.OrderShow.as_view(), name='order_show')
]
