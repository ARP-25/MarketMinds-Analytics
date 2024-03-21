from django.db import models
from subscription.models import SubscriptionPlan

class FinancialMetrics(models.Model):
    """
    Model representing financial metrics for a specific period.

    This model stores financial data related to subscriptions for a given period. 
    It includes fields for tracking the monthly revenue, the number of renewed, new, 
    and canceled subscriptions.

    The model is designed to provide a comprehensive overview of the financial performance 
    of subscription-based services, allowing for analysis and reporting.

    Attributes:
        - period (DateField): The date representing the specific period for which these 
          financial metrics apply.
        - monthly_revenue (DecimalField): Total revenue generated in the specified period.
        - renewed_subscriptions (IntegerField): Number of subscriptions that were renewed 
          during this period.
        - new_subscriptions (IntegerField): Number of new subscriptions acquired during 
          this period.
        - canceled_subscriptions (IntegerField): Number of subscriptions that were canceled 
          during this period.

    Future Enhancements:
        - Fields for tracking revenue from new and canceled subscriptions (currently 
          commented out) could be activated for more detailed financial insights.

    Methods:
        - __str__: Returns a human-readable string representation of the financial metrics 
          for a particular period.

    Notes:
        - This model is essential for tracking and analyzing the financial health and 
          trends of the business over different time periods.
    """
    period = models.DateField()  
    monthly_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  
    renewed_subscriptions = models.IntegerField(default=0)
    new_subscriptions = models.IntegerField(default=0)
    canceled_subscriptions = models.IntegerField(default=0)

    #new_subscription_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    #canceled_subscription_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Financial Metrics for {self.period.strftime('%Y-%m')}"





