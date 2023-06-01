from django.core.exceptions import ValidationError
from django.forms import ModelForm

from order.models import Order
from user.tests import valid_number


class OrderForm(ModelForm):
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if not valid_number(phone_number):
            raise ValidationError('Некорректный номер телефона!')
        return phone_number

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = ''
            self.fields[field].widget.attrs['class'] = 'form-control'

        self.fields['first_name'].widget.attrs['placeholder'] = 'Имя'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Фамилия'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Номер телефона'
        self.fields['city'].widget.attrs['placeholder'] = 'Город'
        self.fields['postal_code'].widget.attrs['placeholder'] = 'Почтовый код'
        self.fields['address'].widget.attrs['placeholder'] = 'Адрес'

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone_number',
                  'city', 'postal_code', 'address']
