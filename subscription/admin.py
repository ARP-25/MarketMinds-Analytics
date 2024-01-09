from django.contrib import admin
from .models import SubscriptionPlan
from django_summernote.admin import SummernoteModelAdmin

@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(SummernoteModelAdmin):
    """
    Admin configuration for SubscriptionPlan model.

    Utilizes Summernote for the 'title' field editing.
    
    Attributes:
    - summernote_fields: Fields utilizing Summernote for rich text editing.
    - list_display: Fields to display in the admin interface.
    - list_filter: Fields available for filtering in the admin interface.
    """
    summernote_fields = ('title')
    list_display = ['title', 'id', 'image', 'description', 'price', 'details']
    list_filter = ['price']


