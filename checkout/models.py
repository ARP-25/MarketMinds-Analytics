from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
import datetime

import stripe

from subscription.models import SubscriptionPlan


class ActiveSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='active_subscriptions')
    subscription_plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    stripe_subscription_id = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    renewal_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True) 
    status = models.CharField(max_length=50, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    billing_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    monthly_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.start_date:
            self.start_date = timezone.now()
        if self.status != 'pending cancellation' and (self.renewal_date is None or not self.pk):
            self.renewal_date = self.start_date + timezone.timedelta(days=30)
        if self.subscription_plan and self.monthly_cost is None:
            self.monthly_cost = self.subscription_plan.price

        super().save(*args, **kwargs)

    def is_expired(self):
        return timezone.now() >= self.renewal_date  

    def refresh_subscription(self):
        if self.is_expired():
            self.renewal_date = timezone.now() + timezone.timedelta(days=30) 
            self.save()

    def cancel_subscription(self):
        """
        Cancel subscription via Stripe API and update renewal_date and end_date.
        """
        try:
            stripe.api_key = settings.STRIPE_SECRET_KEY
            subscription = stripe.Subscription.retrieve(self.stripe_subscription_id)
            stripe.Subscription.modify(
                self.stripe_subscription_id,
                cancel_at_period_end=True
            )
            self.end_date = timezone.make_aware(
                datetime.datetime.fromtimestamp(subscription.current_period_end)
            )
            self.renewal_date = None  
            self.status = 'pending cancellation'
            self.save()
        except stripe.error.StripeError as e:
            print(f"Stripe error: {e}")

    def update_status(self, new_status):
        self.status = new_status
        self.save()

    def __str__(self):
        return f"{self.subscription_plan.title} - {self.user.username} - {self.status}"

