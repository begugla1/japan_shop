from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from .cart import Cart
from .forms import CartAddProductForm


def cart_detail(request):
    form = CartAddProductForm()
    context = {
        'form': form,
    }
    return render(request, 'cart/cart_detail.html', context)


def cart_add(request, product_id):
    cart = Cart(request)

    if request.method == 'POST':
        form_quantity = CartAddProductForm(request.POST)
        if form_quantity.is_valid():
            form_data = form_quantity.cleaned_data
            cart.add(request,
                     product_id,
                     form_data['quantity'],
                     form_data['update']
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