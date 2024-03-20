from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import FinancialMetrics
from checkout.models import ActiveSubscription
from subscription.models import SubscriptionPlan
from django.utils import timezone
from decimal import Decimal


@receiver(post_save, sender=ActiveSubscription)
def update_metrics_on_subscription_update_renew(sender, instance, created, **kwargs):
    print("We are in the signal update new subscription")
    if not created and instance.renewed_at:
        period_start = timezone.now().replace(day=1, hour=0, minute=0, second=0)
        metrics, created = FinancialMetrics.objects.get_or_create(period=period_start)
        metrics.renewed_subscriptions += 1
        metrics.total_revenue += Decimal(instance.monthly_cost)
        metrics.monthly_recurring_revenue += Decimal(instance.monthly_cost)
        metrics.save()

        print("Financial metrics updated for renewed subscription.")



@receiver(post_save, sender=ActiveSubscription)
def update_metrics_on_subscription_update_cancel(sender, instance, created, **kwargs):
    
    # Check if the instance is being updated (not created) and if canceled_at is set
    if not created and instance.canceled_at:
        print("We are in the signal update cancel subscription")
        period_start = timezone.now().replace(day=1, hour=0, minute=0, second=0)
        metrics, created = FinancialMetrics.objects.get_or_create(period=period_start)
        metrics.canceled_subscriptions += 1

        # Ensuring total_revenue field on FinancialMetrics model is Decimal field
        metrics.total_revenue = Decimal(str(metrics.total_revenue))
        metrics.total_revenue -= Decimal(instance.monthly_cost)

        # Ensuring monthly_recurring_revenue field on FinancialMetrics model is Decimal field
        metrics.monthly_recurring_revenue = Decimal(str(metrics.monthly_recurring_revenue))
        metrics.monthly_recurring_revenue -= Decimal(instance.monthly_cost)

        metrics.save()
