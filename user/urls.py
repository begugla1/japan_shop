from django.urls import path

from . import views


urlpatterns = [
    path('user/login', views.HomeLogin.as_view(), name='login'),
    path('user/register', views.HomeRegister.as_view(), name='register'),
    path('user/logout', views.HomeLogout.as_view(), name='logout'),
]
