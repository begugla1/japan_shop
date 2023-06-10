# Generated by Django 4.2.1 on 2023-06-10 13:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0005_alter_profile_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profile_photo",
            field=models.ImageField(
                blank=True,
                upload_to="profile_photos/%Y/%m/%d",
                verbose_name="Фото профиля",
            ),
        ),
    ]