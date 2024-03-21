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
    """
    A Django view function that renders a page with insights organized by stages.

    This function gathers insights from the database, categorizing them into different stages 
    ('Mainstage' and 'Secondstage') for display purposes. It also fetches the list of staged 
    subscription plans to be shown on the same page. The insights are ordered by their 
    release date, ensuring the most recent ones are displayed prominently.

    The 'Mainstage' insights are limited to the four most recent entries, while the 
    'Secondstage' insights include all available entries in that category.

    Args:
    - request (HttpRequest): The Django request object.

    Returns:
    - HttpResponse: Renders the 'trade_insights/trade_insights.html' template with the context 
      containing 'Mainstage' and 'Secondstage' insights, along with staged subscription plans.

    Notes:
    - The function provides a filtered view of insights based on their categorization into 
      different stages, allowing users to browse them based on their relevance and prominence.
    - This view can be adapted or extended to include more insight stages or customized 
      sorting and filtering options.
    """
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
    """
    A Django view function that displays the detail of a specific insight.

    This function retrieves an insight based on its slug and displays detailed information 
    about it. It checks if the current user is subscribed to the category of the insight. 
    If the user is subscribed or the insight's category is in the 'pending cancellation' 
    status, the full content of the insight is shown. Otherwise, only a reduced version 
    of the content is displayed.

    The view also fetches similar insights from the same category to display as 
    recommendations and lists all staged subscription plans for navigation purposes.

    Args:
    - request (HttpRequest): The request object.
    - slug (str): The slug of the insight to be displayed.

    Returns:
    - HttpResponse: Renders the 'trade_insights/trade_insights_detail.html' template with 
      the context containing the insight, similar insights, subscription status, and 
      staged subscription plans.

    Notes:
    - The view uses a 'deepcopy' to create a reduced version of the insight content, 
      ensuring the original insight instance is not modified.
    - This view is intended for users to explore and read insights, with full access 
      depending on their subscription status.
    """
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
        