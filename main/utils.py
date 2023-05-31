from django.db.models import Count

from .models import Category, Product


class HomeMixin:
    paginate_by = 6
    model = Product
    template_name = 'main/home.html'
    context_object_name = 'products'

    def get_user_data(self, **kwargs):
        context = kwargs
        context['cats'] = Category.objects.all().annotate(product_quantity=Count('product'))
        return context

