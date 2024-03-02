from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Insight
from subscription.models import SubscriptionPlan

# Create your views here.
def trade_insights(request):
    ms_insights = Insight.objects.filter(stage='MS')
    ss_insights = Insight.objects.filter(stage='SS')
    sp = SubscriptionPlan.objects.all()
    context = {
        'ms_insights': ms_insights,
        'ss_insights': ss_insights,
        'sp': sp,
    }

    return render(request, 'trade_insights/trade_insights.html', context)