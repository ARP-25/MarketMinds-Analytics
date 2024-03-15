from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import FinancialMetrics
from checkout.models import ActiveSubscription
from subscription.models import SubscriptionPlan
from django.utils import timezone

def update_metrics_on_new_subscription(sender, instance, created, **kwargs):
    if created:
        period_start = timezone.now().replace(day=1, hour=0, minute=0, second=0)
        metrics, created = FinancialMetrics.objects.get_or_create(period=period_start)

        metrics.new_subscriptions += 1
        metrics.total_revenue += instance.monthly_cost
        metrics.monthly_recurring_revenue += instance.monthly_cost
        metrics.save()

@receiver(post_delete, sender=ActiveSubscription)
def update_metrics_on_canceled_subscription(sender, instance, **kwargs):
    period_start = timezone.now().replace(day=1, hour=0, minute=0, second=0)
    metrics, created = FinancialMetrics.objects.get_or_create(period=period_start)

    metrics.canceled_subscriptions += 1
    metrics.total_revenue -= instance.monthly_cost
    metrics.monthly_recurring_revenue -= instance.monthly_cost
    metrics.save()
