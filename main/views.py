from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import *
from .utils import HomeMixin


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

