import datetime
from django.shortcuts import render
from django.http import JsonResponse
from .models import FinancialMetrics
from django.utils import timezone

def get_financial_metrics(request):
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