from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import OrderForm
from cart.cart import Cart
from .models import OrderItem, Order


# TODO пофиксить баг при выходе из формы оплаты через кнопку в браузере
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
        self.request.session['order_id'] = order.id
        self.request.session.modified = True
        return redirect('payment:process')


class OrderShow(ListView):
    model = Order
    template_name = 'order/order_show.html'
    context_object_name = 'orders'
    paginate_by = 3

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


def order_delete(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    return redirect('order_show')


def order_delete_all(request):
    orders = Order.objects.filter(user=request.user)
    orders.delete()
    return redirect('order_show')
