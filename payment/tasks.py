from celery import shared_task
from order.email import send_email_acceptation


@shared_task
def order_created(order_id):
    """Асинхронное задание по отправке email"""
    send_email_acceptation(order_id)
