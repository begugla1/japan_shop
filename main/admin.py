from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'price', 'stock', 'available',
                    'image', 'create_time', 'cat')
    list_display_links = ('name', 'cat')
    list_filter = ('available', 'create_time', 'update_time', 'cat')
    search_fields = ('name', 'cat')
    list_editable = ('available',)
    readonly_fields = ('image',)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name',)
    list_display_links = ('name',)


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Category, CategoryAdmin)
