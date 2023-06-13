import copy

from main.models import Product
from app import settings


class Cart(object):
    def __init__(self, request):
        cart = request.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = request.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __save(self, request):
        request.session[settings.CART_SESSION_ID] = self.cart
        request.session.modified = True

    def add(self, request, product_id, product_quantity=0, product_update=False):
        product = self.cart.get(str(product_id))
        db_product = Product.objects.get(id=product_id)

        if not product:
            self.cart[str(product_id)] = {
                                          'quantity': product_quantity,
                                          'price': db_product.price
                                          }

        if product_update:
            self.cart[str(product_id)]['quantity'] = product_quantity
        else:
            self.cart[str(product_id)]['quantity'] += 1

        self.__save(request)

    def remove(self, request, product_id):
        product = self.cart.get(str(product_id))
        if product:
            del self.cart[str(product_id)]
            self.__save(request)

    def clear(self, request):
        self.cart.clear()
        self.__save(request)

    def __iter__(self):
        cart_copy = copy.deepcopy(self.cart)
        products_ids = cart_copy.keys()
        db_products = Product.objects.filter(id__in=products_ids).select_related('cat')

        for db_product in db_products:
            cart_copy[str(db_product.id)]['product_model'] = db_product

        for product in cart_copy.values():
            product['total_product_sum'] = product['price'] * product['quantity']
            yield product

    def get_total_quantity(self):
        return sum((product['quantity'] for product in self.cart.values()))

    def get_total_sum(self):
        return sum((product['quantity'] * product['price'] for product in self.cart.values()))

    def get_ids(self):
        return (key for key in self.cart.keys())

