from django.contrib import admin
from .models import UserLoginDetails

@admin.register(UserLoginDetails)
class UserLoginDetailsAdmin(admin.ModelAdmin):
    list_display = ('password', 'username', 'email', 'url', 'user', 'site_name')
