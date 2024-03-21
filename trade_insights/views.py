from copy import deepcopy
from django.shortcuts import render
from django.views.generic.list import ListView
from django.db.models import Q
from .models import Insight
from django.shortcuts import render, get_object_or_404
from subscription.models import SubscriptionPlan
from checkout.models import ActiveSubscription

# Create your views here.
def trade_insights(request):
    ms_insights = Insight.objects.filter(stage='MS').order_by('-release_date')[:4]
    ss_insights = Insight.objects.filter(stage='SS')
    sp = SubscriptionPlan.objects.filter(staged=True)
    context = {
        'ms_insights': ms_insights,
        'ss_insights': ss_insights,
        'sp': sp,
    }

    return render(request, 'trade_insights/trade_insights.html', context)

def trade_insights_detail(request, slug):
    staged_subscription_plans = SubscriptionPlan.objects.filter(staged=True)
    insight = get_object_or_404(Insight, slug=slug)
    category = insight.category
    similar_insights = Insight.objects.filter(category=category)
    print(similar_insights)
    user = request.user
    if user.is_authenticated and user.active_subscriptions.filter(
        Q(subscription_plan=insight.category) & 
        (Q(status='active') | Q(status='pending cancellation'))
    ).exists():
        print(f"User is subscribed to {insight.category}")
        subscribed = True

        context = {
            'sp': staged_subscription_plans,
            'subscribed': subscribed,
            'insight': insight,  
            'similar_insights': similar_insights
        }
    else:
        print("User is not subscribed or not authenticated")
        subscribed = False
        reduced_insight = deepcopy(insight)
        reduced_insight.content = reduced_insight.content[:300] + ' ...'
        context = {
            'sp': staged_subscription_plans,
            'subscribed': subscribed,
            'insight': reduced_insight,  
            'similar_insights': similar_insights,
            'subscription_plan': category,
        }
    
    return render(request, 'trade_insights/trade_insights_detail.html', context)
        