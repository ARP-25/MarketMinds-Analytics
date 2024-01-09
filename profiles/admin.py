from django.contrib import admin
from .models import UserProfile
from checkout.models import ActiveSubscription  # Adjust import path as needed


class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for the UserProfile model.

    Displays user-related information such as username, bio, birth date,
    full name, email, phone number, and active subscriptions in the admin interface.

    Attributes:
    - list_display: Fields to display in the admin interface.
    - list_filter: Fields available for filtering in the admin interface.
    - search_fields: Fields available for searching in the admin interface.
    - ordering: Ordering of displayed data in the admin interface.
    """
    list_display = ('user', 'bio', 'birth_date', 'full_name', 'email', 'phone_number', 'get_active_subscriptions')
    list_filter = ('birth_date',)
    search_fields = ('user__username', 'full_name', 'email', 'birth_date', 'email', 'phone_number')
    ordering = ('user__username',)



admin.site.register(UserProfile, UserProfileAdmin)
