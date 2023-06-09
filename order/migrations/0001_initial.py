# Generated by Django 4.2.1 on 2023-07-02 14:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_id', models.CharField(blank=True, max_length=255, verbose_name='Stripe ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=255, verbose_name='Номер телефона')),
                ('city', models.CharField(max_length=255, verbose_name='Город')),
                ('postal_code', models.PositiveIntegerField(verbose_name='Почтовый код')),
                ('address', models.CharField(default='Не указано', max_length=255, verbose_name='Адрес')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время формирования')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('paid', models.BooleanField(default=False, verbose_name='Оплачено')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['-time_create'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('total_cost', models.PositiveIntegerField(default=0, verbose_name='Общая сумма')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Товар заказа',
                'verbose_name_plural': 'Товары заказа',
                'ordering': ['order'],
            },
        ),
    ]
