from django.contrib import admin
from .models import SubscriptionPlan

@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ['image', 'title', 'description', 'price', 'details']
