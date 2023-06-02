import smtplib
from email.mime.text import MIMEText

from order.models import Order


def order_created(order_id):
    """
    Задача для отправки уведомления по email
    :param order_id:
    :return:
    """
    sender = "yokimokiadm@gmail.com"
    password = "aeahwjteaezmgjch"
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

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg['Subject'] = subject
        server.sendmail(sender, order.email, msg.as_string())

    except Exception as _ex:
        return f'{_ex}\nПроверьте введённые данные'

