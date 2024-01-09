from .models import ActiveSubscription
from django.contrib import admin

class ActiveSubscriptionAdmin(admin.ModelAdmin):
    """
    Admin configuration for ActiveSubscription model.

    Displays user, subscription plan, start date, end date, status,
    payment status, and purchase number in the admin interface.
    """
    list_display = ('user', 'subscription_plan', 'start_date', 'end_date', 'status', 'payment_status', 'purchase_number')
    
admin.site.register(ActiveSubscription, ActiveSubscriptionAdmin)


