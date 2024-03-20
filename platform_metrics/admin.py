from .models import PlanMetrics, FinancialMetrics
from django.contrib import admin



class PlanMetricsAdmin(admin.ModelAdmin):

    list_display = ('financial_metrics','subscription_plan','active_subscriptions_count',)

admin.site.register(PlanMetrics, PlanMetricsAdmin)


class FinancialMetricsAdmin(admin.ModelAdmin):



    def get_plan_metrics_display(self, obj):
        # Assuming PlanMetrics has a ForeignKey to FinancialMetrics and SubscriptionPlan
        plan_metrics = PlanMetrics.objects.filter(financial_metrics=obj)
        return ", ".join(plan_metric.subscription_plan.name for plan_metric in plan_metrics)

    get_plan_metrics_display.short_description = 'Plan Metrics'
    
    list_display = ('renewed_subscriptions', 'new_subscriptions','canceled_subscriptions','get_plan_metrics_display')



admin.site.register(FinancialMetrics, FinancialMetricsAdmin)


