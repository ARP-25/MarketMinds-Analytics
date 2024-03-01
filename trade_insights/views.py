from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Insight

# Create your views here.
class TradeInsightsListView(ListView):
    model = Insight
    template_name = 'trade_insights/trade_insights.html'
    context_object_name = 'insights'