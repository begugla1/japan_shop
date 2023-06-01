
from main.models import Product
from app import settings


class Cart(object):
    def __init__(self, request):
        cart = request.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = request.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def save(self, request):
        request.session[settings.CART_SESSION_ID] = self.cart
        request.session.modified = True

    def add(self, request, product_id, product_quantity=0, product_update=False):
        product = self.cart.get(str(product_id))
        db_product = Product.objects.get(id=product_id)

        if not product:
            self.cart[str(product_id)] = {
                                          'quantity': product_quantity,
                                          'price': db_product.price,
                                          }

        if product_update:
            self.cart[str(product_id)]['quantity'] = product_quantity
        else:
            self.cart[str(product_id)]['quantity'] += 1

        self.save(request)

    def remove(self, request, product_id):
        product = self.cart.get(str(product_id))
        if product:
            del self.cart[str(product_id)]
            self.save(request)

    def clear(self, request):
        self.cart.clear()
        self.save(request)

    def __iter__(self):
        products_ids = self.cart.keys()
        db_products = Product.objects.filter(id__in=products_ids)

        for db_product in db_products:
            self.cart[str(db_product.id)]['product_model'] = db_product

        for product in self.cart.values():
            product['total_product_sum'] = product['price'] * product['quantity']
            yield product

    def get_total_quantity(self):
        return sum((product['quantity'] for product in self.cart.values()))

    def get_total_sum(self):
        return sum((product['quantity'] * product['price'] for product in self.cart.values()))

    def get_ids(self):
        return list(key for key in self.cart.keys())

