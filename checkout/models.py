from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from subscription.models import SubscriptionPlan
import uuid


class ActiveSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='active_subscriptions')
    subscription_plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()  
    status = models.CharField(max_length=50)  
    payment_status = models.CharField(max_length=50)  
    created_at = models.DateTimeField(auto_now_add=True)
    purchase_number = models.CharField(max_length=32, null=False, editable=False)

    def _generate_purchase_number(self):
        """
        Generate a unique purchase number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override save method to generate purchase number and handle other operations
        """
        if not self.purchase_number:
            self.purchase_number = self._generate_purchase_number()
        super().save(*args, **kwargs)

    def is_expired(self):
        """
        Check if the subscription has expired
        """
        return self.end_date < timezone.now()

    def refresh_subscription(self):
        """
        Refresh the subscription by extending the end date by 30 days
        """
        if self.is_expired():           
            self.end_date += timezone.timedelta(days=30)
            self.status = 'Active' 
            self.save()

    def __str__(self):
        return f"{self.subscription_plan.title} - Start: {self.start_date}"

