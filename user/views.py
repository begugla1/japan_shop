from django.contrib.auth import login
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from user.forms import CustomLoginForm, CustomRegisterForm


class HomeLogin(LoginView):
    form_class = CustomLoginForm
    template_name = 'user/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class HomeRegister(CreateView):
    form_class = CustomRegisterForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class HomeLogout(LogoutView):
    next_page = 'login'
