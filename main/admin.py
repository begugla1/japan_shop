from django.contrib import admin

from . import models


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Category, CategoryAdmin)
