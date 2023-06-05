from django.template import Library
from django.core.cache import cache

register = Library()


@register.inclusion_tag('main/aside.html')
def show_aside(cat_name, cats):
    context = {
        'cat_name': cat_name,
        'cats': cats
    }
    return context


@register.inclusion_tag('main/content.html')
def show_content(cat_name, products, page_obj, paginator, cart, favorites):
    context = {
        'cat_name': cat_name,
        'products': products,
        'page_obj': page_obj,
        'paginator': paginator,
        'cart': cart,
        'favorites': favorites,
    }
    return context


@register.inclusion_tag('main/paginator.html')
def show_pag(page_obj, paginator):
    context = {
        'page_obj': page_obj,
        'paginator': paginator,
    }
    return context


@register.inclusion_tag('main/card.html')
def show_card(product, cart, favorites):
    context = {
        'product': product,
        'cart': cart,
        'favorites': favorites
    }
    return context


@register.inclusion_tag('main/fav_item.html')
def show_fav_item(product, favorites):
    context = {
        'product': product,
        'favorites': favorites
    }
    return context


@register.inclusion_tag('main/cart_item.html')
def show_cart_item(product, cart):
    context = {
        'product': product,
        'cart': cart
    }
    return context


@register.filter
def cut(value: str, quantity: int):
    value = value.replace('<p>', '').replace('</p>', '')
    return value[:quantity] + '...' if len(value[:quantity]) != len(value) else value


@register.filter
def to_str(value):
    return str(value)
