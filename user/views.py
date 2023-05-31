from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from user.forms import CustomLoginForm, CustomRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile


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
        profile = Profile.objects.create(user=user)
        profile.save()
        return redirect('home')


class HomeLogout(LogoutView):
    next_page = 'login'


class HomeProfile(TemplateView):
    template_name = 'user/user_profile.html'


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(instance=request.user, data=request.POST)
        profile_form = ProfileUpdateForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request,
                      'user/edit_profile.html',
                      context
                      )
