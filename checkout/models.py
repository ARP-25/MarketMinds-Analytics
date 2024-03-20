from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.forms import ValidationError
from django.utils import timezone
import datetime

import stripe

from subscription.models import SubscriptionPlan


class ActiveSubscription(models.Model):
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


