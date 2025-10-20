from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    fieldsets = list(UserAdmin.fieldsets)
    fieldsets[1] =(("Personal info"), {"fields": ("name", "email", "profile_image")})


admin.site.register(User, CustomUserAdmin)
