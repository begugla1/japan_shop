from django.urls import path

from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('<slug:cat_slug>', views.HomeCat.as_view(), name='show_cat'),
    path('<slug:cat_slug>/<slug:product_slug>', views.HomeCatProduct.as_view(), name='show_product')
]
