from django.urls import path
from .views import *


app_name = 'payment'

urlpatterns = [
    path('process/', payment_process, name='process'),
    path('completed/', PaymentComplete.as_view(), name='completed'),
    path('canceled/', PaymentCancel.as_view(), name='canceled'),
]
