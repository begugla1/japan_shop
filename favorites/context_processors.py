from .favorites import Favorites


def favorites(request):
    return {'favorites': Favorites(request)}
