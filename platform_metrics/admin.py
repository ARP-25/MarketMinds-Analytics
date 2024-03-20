from .models import FinancialMetrics
from django.contrib import admin


class FinancialMetricsAdmin(admin.ModelAdmin):
    list_display = ('id', 'period', 'renewed_subscriptions', 'new_subscriptions','canceled_subscriptions', 'monthly_revenue')

admin.site.register(FinancialMetrics, FinancialMetricsAdmin)


