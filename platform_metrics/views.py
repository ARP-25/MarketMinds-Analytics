import datetime
from django.shortcuts import render
from django.http import JsonResponse
from .models import FinancialMetrics
from django.utils import timezone

def get_financial_metrics(request):
    """
    A Django view function that retrieves and returns financial metrics data.

    This function is designed to fetch financial metrics from the FinancialMetrics model for the 
    past twelve months. It filters the FinancialMetrics records based on the 'period' field, ensuring
    that only data from the last year is considered. The fetched data includes total monthly revenue, 
    the number of new, canceled, and renewed subscriptions for each month in this period.

    The function constructs a JSON response containing this data, which can be used to populate 
    frontend components such as charts or tables displaying financial trends over time.

    Args:
    - request (HttpRequest): The Django request object.

    Returns:
    - JsonResponse: A Django JsonResponse object containing the financial metrics data. This includes:
      - labels: A list of month-year labels for the periods covered.
      - revenues: Monthly revenue figures for each period.
      - new_subscriptions: Count of new subscriptions for each period.
      - canceled_subscriptions: Count of canceled subscriptions for each period.
      - renewed_subscriptions: Count of renewed subscriptions for each period.

    Notes:
    - This view is particularly useful for creating dashboard views in admin interfaces or 
      analytics pages, providing a quick overview of financial health and trends.
    - The function assumes that the FinancialMetrics model has a 'period' field representing 
      the time period for the metric, along with fields for various types of subscription data.
    """
    twelve_months_ago = timezone.now() - datetime.timedelta(days=365)

    metrics = FinancialMetrics.objects.filter(
        period__gte=twelve_months_ago
    ).order_by('period')

    data = {
        "labels": [metric.period.strftime("%Y-%m") for metric in metrics],
        "revenues": [float(metric.monthly_revenue) for metric in metrics],
        "new_subscriptions": [metric.new_subscriptions for metric in metrics],
        "canceled_subscriptions": [metric.canceled_subscriptions for metric in metrics],
        "renewed_subscriptions": [metric.renewed_subscriptions for metric in metrics],
    }
    return JsonResponse(data)