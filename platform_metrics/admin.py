from .models import PlanMetrics, FinancialMetrics
from django.contrib import admin



class PlanMetricsAdmin(admin.ModelAdmin):

    list_display = ('financial_metrics','subscription_plan','active_subscriptions_count',)

admin.site.register(PlanMetrics, PlanMetricsAdmin)


class FinancialMetricsAdmin(admin.ModelAdmin):

    list_display = ('new_subscriptions','canceled_subscriptions')

admin.site.register(FinancialMetrics, FinancialMetricsAdmin)


