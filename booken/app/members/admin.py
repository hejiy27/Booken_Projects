from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        ('추가필드', {'fields':(
            'nickname',
            'img_profile',
            'attachment'
        )}),
    ) + BaseUserAdmin.fieldsets