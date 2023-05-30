from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import *
from .utils import HomeMixin
from .forms import *


class Home(HomeMixin, ListView):

    def get_queryset(self):
        return Product.objects.filter(available=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_context = self.get_user_data(title='Каталог',
                                           cat_name=None)
        context.update(extra_context)

        return context


class HomeCat(HomeMixin, ListView):

    def get_queryset(self):
        return Product.objects.filter(available=True, cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        el = get_object_or_404(Category, slug=self.kwargs['cat_slug'])
        extra_context = self.get_user_data(title=f'Товары категории: {el}',
                                           cat_name=el)
        context.update(extra_context)
        return context


class HomeCatProduct(DetailView):
    model = Product
    template_name = 'main/product_detail.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class HomeLogin(LoginView):
    form_class = CustomLoginForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class HomeRegister(CreateView):
    form_class = CustomRegisterForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class HomeLogout(LogoutView):
    next_page = 'login'
