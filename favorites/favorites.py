from app import settings
from main.models import Product


class Favorites(object):
    """Class for favorites"""
    def __init__(self, request):
        favorites = request.session.get(settings.FAVORITES_SESSION_ID)
        if not favorites:
            favorites = request.session[settings.FAVORITES_SESSION_ID] = {}
        self.favorites = favorites

    def save(self, request):
        request.session[settings.FAVORITES_SESSION_ID] = self.favorites
        request.session.modified = True

    def add(self, request, product_id):
        is_exists = self.favorites.get(str(product_id))
        if not is_exists:
            self.favorites[str(product_id)] = 1
        self.save(request)

    def delete(self, request, product_id):
        is_exists = self.favorites.get(str(product_id))
        if is_exists:
            del self.favorites[str(product_id)]
        self.save(request)

    def clear(self, request):
        self.favorites.clear()
        self.save(request)

    def __iter__(self):
        products_keys = self.favorites.keys()
        db_products = Product.objects.filter(id__in=products_keys)
        for db_product in db_products:
            yield db_product

    def get_ids(self):
        return (key for key in self.favorites.keys())

    def get_total_quantity(self):
        return len(self.favorites)
