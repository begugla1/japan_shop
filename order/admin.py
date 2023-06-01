from django.contrib import admin
from .models import *


class OrderItemAdmin(admin.ModelAdmin):
    model = OrderItem
    list_display = ('__str__', 'order', 'product', 'quantity', 'price', 'total_cost')
    list_display_links = ('order',)
    list_filter = ('order', 'product')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email',
                    'phone_number', 'city', 'postal_code', 'address',
                    'time_create', 'time_update', 'paid')
    list_display_links = ('user',)
    list_filter = ('user', 'paid', 'time_create')
    list_editable = ('paid',)
    search_fields = ('user', 'first_name', 'last_name')


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)


