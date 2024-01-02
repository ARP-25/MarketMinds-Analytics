from django.shortcuts import get_object_or_404
from subscription.models import SubscriptionPlan


def bag_contents(request):

    bag_items = request.session.get('bag_items', [])

    # Retrieve SubscriptionPlan objects based on their IDs
    subscription_plans = SubscriptionPlan.objects.filter(id__in=bag_items)
    
    # Calculate total price by summing the prices of SubscriptionPlan objects
    total = sum(plan.price for plan in subscription_plans)
        
    context = {
        'bag_items': bag_items,
        'total': total,
        'subscription_plans': subscription_plans,
    }

    return context