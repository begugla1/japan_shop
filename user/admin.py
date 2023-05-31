from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'profile_photo')


admin.site.register(Profile, ProfileAdmin)
