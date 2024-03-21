from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class UserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')

# Unregister the default UserAdmin
admin.site.unregister(User)
# Register the custom UserAdmin
admin.site.register(User, UserAdmin)