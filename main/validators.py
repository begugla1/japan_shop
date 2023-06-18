from django.forms import ValidationError


def price_validate(value):
    if int(value) < 50:
        raise ValidationError('Цена товара не может быть менее 50 рублей!')
    