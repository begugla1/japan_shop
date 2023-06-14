from typing import Any
from django import http
from django.shortcuts import render, redirect, get_object_or_404
import stripe
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from cart.cart import Cart
from payment.tasks import order_created
from order.models import Order

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


class PaymentProcess(TemplateView):

    def get(self, request, *args, **kwargs):
        order_id = request.session.get('order_id', None)
        order = get_object_or_404(Order, id=order_id)

        success_url = request.build_absolute_uri(
            reverse_lazy('payment:completed'))
        cancel_url = request.build_absolute_uri(
            reverse_lazy('payment:canceled'))
        # Stripe session data
        session_data = {
            'mode': 'payment',
            'client_reference_id': order.id,
            'success_url': success_url,
            'cancel_url': cancel_url,
            'line_items': []
        }
        for item in order.orderitem_set.all():
            session_data['line_items'].append({
                'price_data': {
                    'unit_amount': item.price * 100,
                    'currency': 'rub',
                    'product_data': {
                        'name': item.product.name
                    },
                },
                'quantity': item.quantity
            })

        session = stripe.checkout.Session.create(**session_data)

        return redirect(session.url, code=303)


class PaymentComplete(TemplateView):

    def get(self, request, *args, **kwargs):
        order_id = request.session['order_id']
        order = get_object_or_404(Order, id=order_id)
        order.paid = True
        order.save()
        cart = Cart(self.request)
        cart.clear(self.request)
        order.get_away_bought_products()
        order_created.delay(order.id)
        return render(self.request, 'payment/completed.html')


class PaymentCancel(TemplateView):
    template_name = 'payment/canceled.html'

    def get(self, request, *args, **kwargs):
        cart = Cart(self.request)
        cart.clear(self.request)
        order_id = request.session['order_id']
        order = get_object_or_404(Order, id=order_id)
        order.delete()
        return render(self.request, 'payment/canceled.html')
