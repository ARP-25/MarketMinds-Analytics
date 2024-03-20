from django.db import models
from subscription.models import SubscriptionPlan

class FinancialMetrics(models.Model):
    period = models.DateField()  
    monthly_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  
    renewed_subscriptions = models.IntegerField(default=0)
    new_subscriptions = models.IntegerField(default=0)
    canceled_subscriptions = models.IntegerField(default=0)

    #new_subscription_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    #canceled_subscription_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Financial Metrics for {self.period.strftime('%Y-%m')}"





