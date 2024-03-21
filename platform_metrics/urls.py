from django.urls import path
from .views import get_financial_metrics

urlpatterns = [
    # ... your other urls
    path('api/financial-metrics/', get_financial_metrics, name='financial-metrics'),
]