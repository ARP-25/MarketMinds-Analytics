from django.contrib import admin

from .models import ActiveSubscription


class ActiveSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'subscription_plan', 'start_date', 'end_date', 'status', 'payment_status', 'purchase_number')
    
admin.site.register(ActiveSubscription, ActiveSubscriptionAdmin)


