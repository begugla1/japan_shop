from django.core.mail import send_mail

from order.models import Order
from app import settings


def order_created(order_id):
    """
    Отправка уведомления по email
    :param order_id:
    :return:
    """
    order = Order.objects.get(id=order_id)
    subject = f'<<< Вы оформили заказ в магазине Ёки Моки >>>'
    message = f'''Дорогой {order.first_name} {order.last_name},\n\n
                Ваш заказ был оформлен успешно!\n
                Дата оформления заказа: {order.time_create}\n
                Номер заказа: {order.id}\n
                Адрес: Город - {order.city}; почтовый код - {order.postal_code}; адрес - {order.address}\n
                Будем ждать вас еще!\n
                С уважением, администрация Ёки Моки.
                '''

    send_mail(subject, message, settings.EMAIL_HOST_USER, [order.email])

