from django.urls import path
from .views import *


app_name = 'payment'

urlpatterns = [
    path('process/', PaymentProcess.as_view(), name='process'),
    path('completed/', PaymentComplete.as_view(), name='completed'),
    path('canceled/', PaymentCancel.as_view(), name='canceled'),
]
