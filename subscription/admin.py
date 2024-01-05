from django.contrib import admin
from .models import SubscriptionPlan
from django_summernote.admin import SummernoteModelAdmin

@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(SummernoteModelAdmin):
    summernote_fields = ('title')
    list_display = ['title', 'id', 'image', 'description', 'price', 'details']
    list_filter = ['price']


