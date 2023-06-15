from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


class OrderItemAdmin(admin.ModelAdmin):
    model = OrderItem
    list_display = ('__str__', 'order', 'product', 'quantity', 'price', 'total_cost')
    list_display_links = ('order',)
    list_filter = ('order', 'product')


def order_stripe_payment(obj):
    url = obj.get_order_stripe_url()
    if obj.stripe_id:
        html = f'<a href="{url}" target="_blank">{obj.stripe_id}</a>'
        return mark_safe(html)
    return ''
order_stripe_payment.short_description = 'Stripe payment'


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email',
                    'phone_number', 'city', 'postal_code', 'address',
                    order_stripe_payment, 'time_create', 'time_update', 
                    'paid')
    list_display_links = ('user',)
    list_filter = ('user', 'paid', 'time_create')
    list_editable = ('paid',)
    search_fields = ('user', 'first_name', 'last_name')


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)


