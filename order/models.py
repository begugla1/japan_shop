from django.conf import settings
from django.db import models

from main.models import Product


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_index=True,
                             verbose_name='Пользователь')
    stripe_id = models.CharField('Stripe ID', max_length=255, blank=True)
    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)
    email = models.EmailField('Email')
    phone_number = models.CharField('Номер телефона', max_length=255)
    city = models.CharField('Город', max_length=255)
    postal_code = models.PositiveIntegerField('Почтовый код')
    address = models.CharField('Адрес', max_length=255, default='Не указано')
    time_create = models.DateTimeField('Время формирования', auto_now_add=True)
    time_update = models.DateTimeField('Время обновления', auto_now=True)
    paid = models.BooleanField('Оплачено', default=False)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-time_create']

    def __str__(self):
        return f'Заказ пользователя {self.user} номер {self.pk}'

    def get_total_sum(self):
        return sum(item.total_cost for item in self.orderitem_set.all())

    def get_total_quantity(self):
        return sum(item.quantity for item in self.orderitem_set.all())

    def get_away_bought_products(self):
        order_items = self.orderitem_set.all()
        order_db_products = (order_item.product for order_item in order_items)
        for db_product in order_db_products:
            db_product.stock -= order_items.get(product=db_product).quantity
            db_product.save()

    def get_order_stripe_url(self):
        if not self.stripe_id:
            return ''
        path = '/test/' if '_test_' in settings.STRIPE_SECRET_KEY else '/'
        return f'https://dashboard.stripe.com{path}payments/{self.stripe_id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, db_index=True, verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_index=True, verbose_name='Товар')
    quantity = models.PositiveIntegerField('Количество')
    price = models.PositiveIntegerField('Цена')
    total_cost = models.PositiveIntegerField('Общая сумма', default=0)

    class Meta:
        verbose_name = 'Товар заказа'
        verbose_name_plural = f'Товары заказа'
        ordering = ['order']

    def __str__(self):
        return f'Товар {self.product} заказа номер {self.order.pk}'
