from django.shortcuts import render, get_object_or_404, redirect

from .cart import Cart
from .forms import CartAddProductForm


def cart_detail(request):
    cart = Cart(request)
    form = CartAddProductForm()
    context = {
        'cart': cart,
        'form': form,
    }
    return render(request, 'cart/cart_detail.html', context)


def cart_add(request, product_id):
    cart = Cart(request)
    cart.add(request, product_id)
    context = {
        'cart': cart
    }
    return redirect('home')


def cart_remove(request, product_id):
    cart = Cart(request)
    cart.remove(request, product_id)
    context = {
        'cart': cart
    }
    return redirect('home')
