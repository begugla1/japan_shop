from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from user.models import Profile
from user.tests import valid_number


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = ''

        self.fields['username'].widget.attrs['placeholder'] = 'Логин'
        self.fields['password'].widget.attrs['placeholder'] = 'Пароль'


class CustomRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = ''
            self.fields[field].widget.attrs['class'] = 'form-control'

        self.fields['username'].widget.attrs['placeholder'] = 'Логин'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Имя (Не обязательно)'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Фамилия (Не обязательно)'
        self.fields['email'].widget.attrs['placeholder'] = 'Email (Не обязательно)'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UserUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = ''

        self.fields['first_name'].widget.attrs['placeholder'] = 'Имя'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Фамилия'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileUpdateForm(ModelForm):

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if not valid_number(phone_number):
            raise ValidationError('Некорректный номер телефона!')
        return phone_number

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = ''

        self.fields['phone_number'].widget.attrs['placeholder'] = 'Номер телефона'
        self.fields['profile_photo'].widget.attrs['placeholder'] = 'Фото профиля'

        self.fields['profile_photo'].label = 'Фото профиля'

    class Meta:
        model = Profile
        fields = ['phone_number', 'profile_photo']
