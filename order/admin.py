from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
import csv
import datetime
from django.http import HttpResponse


class OrderItemAdmin(admin.ModelAdmin):
    model = OrderItem
    list_display = ('__str__', 'order', 'product', 'quantity', 'price', 'total_cost')
    list_display_links = ('order',)
    list_filter = ('order', 'product')


# Creating of url to stripe payment
def order_stripe_payment(obj):
    url = obj.get_order_stripe_url()
    if obj.stripe_id:
        html = f'<a href="{url}" target="_blank">{obj.stripe_id}</a>'
        return mark_safe(html)
    return ''


order_stripe_payment.short_description = 'Stripe payment'


# Export order information to csv file
def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    filename = "Yoki-Moki orders inforamtion.csv"
    response = HttpResponse(
        content_type='text/csv',
        headers={
            'Content-Disposition': 'attachment;'
            f'filename={filename}'
        }
    )
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() \
              if not (field.many_to_many or field.one_to_many)]
    # Первая строка заголовка
    writer.writerow([field.verbose_name for field in fields])
    # Строки данных
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)

    return response


export_to_csv.short_description = 'Экспорт в CSV'


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email',
                    'phone_number', 'city', 'postal_code', 'address',
                    order_stripe_payment, 'time_create', 'time_update',
                    'paid')
    list_display_links = ('user',)
    list_filter = ('user', 'paid', 'time_create')
    list_editable = ('paid',)
    search_fields = ('user', 'first_name', 'last_name')
    actions = [export_to_csv]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)


