from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    phone_number = models.CharField('Номер телефона', max_length=100, blank=True, null=True)
    profile_photo = models.ImageField('Фото профиля', upload_to='profile_photos/%Y/%m/%d', blank=True)

    def __str__(self):
        return f'Профиль пользователя {self.user.username}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = ['user']