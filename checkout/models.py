from django.db import models
from django.contrib.auth.models import User
from subscription.models import SubscriptionPlan
import stripe
from django.utils import timezone

class ActiveSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='active_subscriptions')
    subscription_plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    stripe_subscription_id = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    renewal_date = models.DateTimeField()
    status = models.CharField(max_length=50, default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.start_date:
            self.start_date = timezone.now()
        self.renewal_date = self.start_date + timezone.timedelta(days=30)  # Updated field name

        super().save(*args, **kwargs)

    def is_expired(self):
        return timezone.now() >= self.renewal_date  # Updated field name

    def refresh_subscription(self):
        if self.is_expired():
            self.renewal_date = timezone.now() + timezone.timedelta(days=30)  # Updated field name
            self.save()

    def cancel_subscription(self):
        # Logic to cancel subscription via Stripe API
        try:
            stripe.api_key = 'your_stripe_api_key'
            stripe.Subscription.delete(self.stripe_subscription_id)
            self.status = 'cancelled'
            self.save()
        except stripe.error.StripeError as e:
            # Handle error
            print(f"Stripe error: {e}")

    def update_status(self, new_status):
        # Logic to update subscription status based on Stripe webhook data or API response
        self.status = new_status
        self.save()

    def __str__(self):
        return f"{self.subscription_plan.title} - {self.user.username} - {self.status}"

