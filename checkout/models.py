from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.forms import ValidationError
from django.utils import timezone
import datetime

import stripe

from subscription.models import SubscriptionPlan


class ActiveSubscription(models.Model):
    """
    Represents an active subscription of a user.

    This model stores information about users' subscriptions, including the associated 
    user, the subscription plan, and various timestamps relevant to the subscription's 
    lifecycle. It also includes the Stripe subscription ID for integration with the Stripe 
    payment platform.

    Attributes:
    - user (ForeignKey to User): The user who owns the subscription.
    - subscription_plan (ForeignKey to SubscriptionPlan): The plan to which the user is subscribed.
    - stripe_subscription_id (CharField): The ID of the subscription in Stripe.
    - start_date (DateTimeField): The date and time when the subscription started.
    - current_period_end (DateTimeField): The end date and time of the current subscription period.
    - renewal_date (DateTimeField): The date and time when the subscription is scheduled to renew.
    - canceled_at (DateTimeField): The date and time when the subscription was canceled.
    - status (CharField): The current status of the subscription (e.g., 'active', 'cancelled').
    - created_at (DateTimeField): The date and time when the subscription record was created.
    - billing_amount (DecimalField): The amount thats left to be billed for the subscription.
    - monthly_cost (DecimalField): The monthly cost of the subscription.

    Methods:
    - cancel_subscription: Cancels the subscription via the Stripe API.
    - update_status: Updates the status of the subscription.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='active_subscriptions')
    subscription_plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    stripe_subscription_id = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    current_period_end = models.DateTimeField(null=True, blank=True)
    renewal_date = models.DateTimeField(null=True, blank=True)
    canceled_at = models.DateTimeField(null=True, blank=True) 
    status = models.CharField(max_length=50, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    billing_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    monthly_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


    def cancel_subscription(self):
        """
        Cancel subscription via Stripe API and update renewal_date and canceled_at.
        """
        if self.canceled_at is not None:
            raise ValidationError("Subscription cannot be cancelled because it is already cancelled.")
        try:
            stripe.api_key = settings.STRIPE_SECRET_KEY
            stripe.Subscription.modify(
                self.stripe_subscription_id,
                cancel_at_period_end=True
            )
        except stripe.error.StripeError as e:
            print(f"Stripe error: {e}")


    def update_status(self, new_status):
        self.status = new_status
        self.save()


    def __str__(self):
        return f"{self.subscription_plan.title} - {self.user.username} - {self.status}"


