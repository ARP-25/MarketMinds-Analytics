from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import FinancialMetrics
from checkout.models import ActiveSubscription
from subscription.models import SubscriptionPlan
from django.utils import timezone
from decimal import Decimal



@receiver(post_save, sender=ActiveSubscription)
def update_metrics_on_subscription_update(sender, instance, created, **kwargs):
    period_start = timezone.now().replace(day=1, hour=0, minute=0, second=0)
    metrics, _ = FinancialMetrics.objects.get_or_create(period=period_start)
    
    if created:
        # For a new subscription
        metrics.new_subscriptions += 1
        metrics.monthly_revenue += Decimal(instance.monthly_cost)

    elif instance.canceled_at:
        print("Signal cancelled received for: ", instance)
        # For a cancellation
        metrics.canceled_subscriptions += 1
        metrics.monthly_revenue -= Decimal(instance.monthly_cost)
        
    elif instance.renewal_date:
        print("Signal renewal received for: ", instance)
        # For a renewal
        metrics.renewed_subscriptions += 1
        metrics.monthly_revenue += Decimal(instance.monthly_cost)

    metrics.save()
