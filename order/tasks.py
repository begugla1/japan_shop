from celery import shared_task
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

from .models import Order


@shared_task
def order_created(order_id):
    """
    Задача для отправки уведомления по email
    :param order_id:
    :return:
    """
    order = get_object_or_404(Order, id=order_id)
    subject = f'<<< Вы оформили заказ в магазине Ёки Моки >>>'
    message = f'''Дорогой {order.first_name} {order.last_name},\n\n
                Ваш заказ был оформлен успешно!\n
                Дата оформления заказа: {order.time_create}\n
                Номер заказа: {order.id}\n
                Адрес: Город - {order.city}; почтовый код - {order.postal_code}; адрес - {order.address}\n
                Будем ждать вас еще!\n
                С уважением, администрация Ёки Моки.
                '''
    mail_sent = send_mail(subject=subject,
                          message=message,
                          from_email=None,
                          recipient_list=[order.email],
                          )
    return mail_sent

