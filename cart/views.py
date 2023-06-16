from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .cart import Cart


class CartDetail(TemplateView):
    template_name = 'cart/cart_detail.html'


def cart_add(request, product_id):
    cart = Cart(request)

    if request.method == 'POST':
        product_quantity = int(request.POST.get('product_quantity'))
        cart.add(
            request,
            product_id,
            product_quantity,
            True
        )
    else:
        cart.add(request, product_id)

    return redirect(request.META.get('HTTP_REFERER'))


def cart_remove(request, product_id):
    cart = Cart(request)
    cart.remove(request, product_id)
    return redirect(request.META.get('HTTP_REFERER'))


def cart_clear(request):
    cart = Cart(request)
    cart.clear(request)
    return redirect(request.META.get('HTTP_REFERER'))
