# Generated by Django 4.2.1 on 2023-06-01 09:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="address",
            field=models.CharField(
                default="Not stated", max_length=255, verbose_name="Адрес"
            ),
        ),
    ]
