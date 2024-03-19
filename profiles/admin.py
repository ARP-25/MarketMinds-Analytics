from django.contrib import admin
from .models import UserProfile
from checkout.models import ActiveSubscription  


class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for the UserProfile model.

    Displays user-related information such as username, email and active subscriptions in the admin interface.

    Attributes:
    - list_display: Fields to display in the admin interface.
    - list_filter: Fields available for filtering in the admin interface.
    - search_fields: Fields available for searching in the admin interface.
    - ordering: Ordering of displayed data in the admin interface.
    """
    list_display = ('user', 'id', 'email', 'get_active_subscriptions')
    search_fields = ('user__username', 'email',)
    ordering = ('user__username',)


admin.site.register(UserProfile, UserProfileAdmin)
