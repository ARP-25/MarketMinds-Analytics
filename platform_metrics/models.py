from django.db import models
from subscription.models import SubscriptionPlan

class FinancialMetrics(models.Model):
    period = models.DateField()

    total_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    monthly_recurring_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    

    new_subscriptions = models.IntegerField(default=0)
    canceled_subscriptions = models.IntegerField(default=0)

    new_subscription_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    canceled_subscription_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    plan_metrics = models.ManyToManyField(SubscriptionPlan, through='PlanMetrics')

    def update_plan_metrics(self, subscription_plan, change):
        """
        Aktualisiert die Metriken für einen bestimmten Abonnementplan.
        - subscription_plan: Instanz von SubscriptionPlan
        - change: Die Anzahl der Änderungen (positiv für neue Abonnements, negativ für Kündigungen)
        """
        plan_metrics, created = self.plan_metrics.get_or_create(subscription_plan=subscription_plan)
        plan_metrics.active_subscriptions_count += change
        plan_metrics.save()

    def __str__(self):
        return f"Financial Metrics for {self.period.strftime('%Y-%m')}"


class PlanMetrics(models.Model):
    financial_metrics = models.ForeignKey(FinancialMetrics, on_delete=models.CASCADE)
    subscription_plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    active_subscriptions_count = models.IntegerField(default=0)



