from django.contrib import admin
from .models import Insight

@admin.register(Insight)
class InsightAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'release_date', 'category')
    search_fields = ('title', 'content')
 
