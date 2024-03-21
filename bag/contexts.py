from django.shortcuts import get_object_or_404
from subscription.models import SubscriptionPlan


def bag_contents(request):
    """
    Context processor for managing the contents of the shopping bag.

    This function is responsible for retrieving the subscription plans stored in the user's 
    session (identified as 'bag_items') and calculating the total cost. It is used to 
    persist the state of the user's shopping bag across different pages of the site.

    The function first fetches the list of subscription plan IDs stored in the session. 
    Using these IDs, it retrieves the corresponding SubscriptionPlan objects from the database. 
    It then calculates the total cost of these plans, which is used for displaying the 
    subtotal in the shopping bag.

    Args:
    - request (HttpRequest): The HttpRequest object.

    Returns:
    - dict: A context dictionary containing the list of bag items (subscription plan IDs), 
      the total cost of these items, and the corresponding SubscriptionPlan objects. This 
      context is made available to all templates rendered using RequestContext.

    Notes:
    If this key is not present, an empty list is used as the default.
    """
    bag_items = request.session.get('bag_items', [])
    subscription_plans = SubscriptionPlan.objects.filter(id__in=bag_items)
    total = sum(plan.price for plan in subscription_plans)   
    context = {
        'bag_items': bag_items,
        'total': total,
        'subscription_plans': subscription_plans,
    }

    return context