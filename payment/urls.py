from django.urls import path
from .views import *
from .webhooks import stripe_webhook


app_name = 'payment'

urlpatterns = [
    path('process/', PaymentProcess.as_view(), name='process'),
    path('completed/', PaymentComplete.as_view(), name='completed'),
    path('canceled/', PaymentCancel.as_view(), name='canceled'),
    path('webhook/', stripe_webhook, name='stripe-webhook'),
]
