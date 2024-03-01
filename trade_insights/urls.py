from django.urls import path
from .views import TradeInsightsListView

urlpatterns = [
    path('', TradeInsightsListView.as_view(), name='trade_insights'),

]
