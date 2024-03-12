from .models import ActiveSubscription
from django.contrib import admin

class ActiveSubscriptionAdmin(admin.ModelAdmin):
    """
    Admin configuration for ActiveSubscription model.

    Displays user, subscription plan, Stripe subscription ID, status, and purchase number in the admin interface.
    """
    list_display = ('user', 'subscription_plan', 'monthly_cost', 'stripe_subscription_id', 'status', 'start_date', 'renewal_date', 'end_date', 'billing_amount')

admin.site.register(ActiveSubscription, ActiveSubscriptionAdmin)

