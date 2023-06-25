import stripe
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from app import settings
from order.models import Order
from payment.tasks import order_created


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']

    try:
        event = stripe.Webhook.construct_event(
            payload, 
            sig_header,
            settings.STRIPE_WEBHOOK_SECRET)
    except ValueError or stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)
    
    if event.type == 'checkout.session.completed':
        session = event.data.object
        if session.mode == 'payment' and session.payment_status == 'paid':
            order = get_object_or_404(Order, id=session.client_reference_id)
            order.paid = True
            order.stripe_id = session.payment_intent
            order.save()
            order.get_away_bought_products()
            order_created.delay(order.id)
    
    return HttpResponse(status=200)
