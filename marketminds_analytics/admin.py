from django.contrib import admin
from django.contrib.auth.models import User
from .models import ActiveSubscription

User = get_user_model()

class ActiveSubscriptionInline(admin.TabularInline):
    model = ActiveSubscription
    extra = 0  # Set this to control the number of inline forms displayed

class CustomUserAdmin(admin.ModelAdmin):
    model = User
    inlines = [ActiveSubscriptionInline]

admin.site.unregister(User)  # Unregister the default User admin
admin.site.register(User, CustomUserAdmin)  # Register the custom User admin
