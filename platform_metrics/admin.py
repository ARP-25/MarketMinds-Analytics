from .models import FinancialMetrics
from django.contrib import admin


class FinancialMetricsAdmin(admin.ModelAdmin):
    """
    Custom Admin class for the FinancialMetrics model in Django admin.

    This class customizes the display of the FinancialMetrics model in the Django admin interface. 
    It defines how the list of FinancialMetrics instances is displayed, including the choice of 
    fields to be shown in the list view.

    Attributes:
        - list_display: A tuple specifying the fields of the FinancialMetrics model to be displayed 
          in the admin list view. It includes the ID, period, count of renewed, new, and canceled 
          subscriptions, as well as the monthly revenue.

    Notes:
        - This class enhances the admin interface's usability by providing a clear and concise 
          view of the key metrics for financial data.
        - Additional customizations, such as search fields, filter options, and detailed views for 
          each financial metric instance, can be added as needed to further improve the admin 
          experience.
    """
    list_display = ('id', 'period', 'renewed_subscriptions', 'new_subscriptions','canceled_subscriptions', 'monthly_revenue')

admin.site.register(FinancialMetrics, FinancialMetricsAdmin)


