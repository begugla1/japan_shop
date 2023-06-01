from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from .forms import OrderForm
from cart.cart import Cart
from .models import OrderItem, Order


class OrderCreate(LoginRequiredMixin, CreateView):
    form_class = OrderForm
    template_name = 'order/order_create.html'
    success_url = reverse_lazy('order_success')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        order = form.save(commit=False)
        order.user = self.request.user
        order.save()
        cart = Cart(self.request)
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product_model'],
                quantity=item['quantity'],
                price=item['price'],
                total_cost=item['total_product_sum'])
        cart.clear(self.request)
        return redirect('order_success')


class OrderSuccess(TemplateView):
    template_name = 'order/order_success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['order'] = Order.objects.first()
        return context


class OrderShow(ListView):
    model = Order
    paginate_by = 3
    template_name = 'order/order_show.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
