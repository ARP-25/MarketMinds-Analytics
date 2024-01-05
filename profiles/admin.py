from django.contrib import admin
from .models import UserProfile
from checkout.models import ActiveSubscription  # Adjust import path as needed


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'birth_date', 'full_name', 'email', 'phone_number', 'get_active_subscriptions')
    list_filter = ('birth_date',)
    search_fields = ('user__username', 'full_name', 'email', 'birth_date', 'email', 'phone_number')
    ordering = ('user__username',)



admin.site.register(UserProfile, UserProfileAdmin)
