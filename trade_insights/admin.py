from django.contrib import admin
from .models import Insight
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Insight)
class InsightAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'release_date', 'category')
    search_fields = ('title', 'content')
    summernote_fields = ('content',)
