from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Insight
from django.shortcuts import render, get_object_or_404
from subscription.models import SubscriptionPlan

# Create your views here.
def trade_insights(request):
    ms_insights = Insight.objects.filter(stage='MS')
    ss_insights = Insight.objects.filter(stage='SS')
    sp = SubscriptionPlan.objects.filter(staged=True)
    context = {
        'ms_insights': ms_insights,
        'ss_insights': ss_insights,
        'sp': sp,
    }

    return render(request, 'trade_insights/trade_insights.html', context)

def trade_insights_detail(request, slug):
    sp = SubscriptionPlan.objects.all()
    insight = get_object_or_404(Insight, slug=slug)
    category = insight.category
    similiar_insights = Insight.objects.filter(category=category)
    context = {
        'sp': sp,
        'insight': insight,
        'similiar_insights': similiar_insights
    }

    return render(request, 'trade_insights/trade_insights_detail.html', context)