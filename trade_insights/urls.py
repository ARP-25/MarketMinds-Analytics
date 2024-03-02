from django.urls import path
from .views import trade_insights, trade_insights_detail

urlpatterns = [
    path('', trade_insights, name='trade_insights'),
    path('trade-insights-detail/<slug:slug>/', trade_insights_detail, name='trade_insights_detail'),
]
