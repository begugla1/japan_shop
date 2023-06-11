from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'price', 'stock', 'available',
                    'get_html_photo', 'create_time', 'cat')
    list_display_links = ('name', 'cat')
    list_filter = ('available', 'create_time', 'update_time', 'cat')
    search_fields = ('name', 'cat')
    list_editable = ('available',)
    readonly_fields = ('create_time', 'update_time')
    fields = ('name', 'slug', 'image', 'description', 'price',
              'available', 'stock', 'cat')

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f'<img src="{object.image.url}" height=40')

    get_html_photo.short_description = 'Картинка'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name',)
    list_display_links = ('name',)


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Category, CategoryAdmin)

admin.AdminSite.site_header = 'Администрация Йоки Моки'
admin.AdminSite.site_title = 'Йоки Моки'
admin.AdminSite.index_title = 'Администрация магазина'
