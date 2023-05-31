from django.urls import path

from . import views


urlpatterns = [
    path('login', views.HomeLogin.as_view(), name='login'),
    path('register', views.HomeRegister.as_view(), name='register'),
    path('logout', views.HomeLogout.as_view(), name='logout'),
    path('profile', views.HomeProfile.as_view(), name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile')
]
