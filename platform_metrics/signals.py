from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import FinancialMetrics
from checkout.models import ActiveSubscription
from subscription.models import SubscriptionPlan
from django.utils import timezone
from decimal import Decimal



@receiver(post_save, sender=ActiveSubscription)
def update_metrics_on_subscription_update(sender, instance, created, **kwargs):
    """
    Signal receiver for post-save events on the ActiveSubscription model.

    This function updates the financial metrics whenever a subscription is created, 
    renewed, or canceled. It ensures that the FinancialMetrics model reflects the 
    latest state of subscriptions, providing an accurate picture of the business's 
    financial performance.

    The function operates by identifying the type of subscription event (creation, 
    cancellation, renewal) and adjusting the count and revenue figures in the 
    FinancialMetrics model accordingly.

    Args:
    - sender: The model class that sent the signal.
    - instance: The actual instance being saved.
    - created (bool): A flag indicating whether this is a new record creation.
    - kwargs: Additional keyword arguments.

    Logic:
    - For new subscriptions, increments the 'new_subscriptions' count and adds the 
      subscription cost to 'monthly_revenue'.
    - For cancellations, increments the 'canceled_subscriptions' count and subtracts the 
      subscription cost from 'monthly_revenue'.
    - For renewals, increments the 'renewed_subscriptions' count and adds the 
      subscription cost to 'monthly_revenue'.

    Notes:
    - This function is connected to the post-save signal of the ActiveSubscription 
      model, meaning it gets automatically invoked after a save operation on an 
      ActiveSubscription instance.
    - The function identifies the current period (month) and updates or creates a 
      FinancialMetrics record for that period.
    """
    period_start = timezone.now().replace(day=1, hour=0, minute=0, second=0)
    metrics, _ = FinancialMetrics.objects.get_or_create(period=period_start)
    
    # Ensure that monthly_revenue is treated as a Decimal
    metrics.monthly_revenue = Decimal(metrics.monthly_revenue)

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
