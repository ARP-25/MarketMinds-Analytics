from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from subscription.models import SubscriptionPlan


def bag(request):
    """
    A View to return bag page
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request):
    """
    Add a subscription plan to the user's shopping bag.

    Args:
        request: The HTTP request object.

    Returns:
        Redirects to the 'get_started' page after adding the subscription plan to the bag.
    """
    if request.method == 'POST':
        subscription_plan_id = request.POST.get('subscription_plan_id')
        subscription_plan = get_object_or_404(SubscriptionPlan, id=subscription_plan_id)
        bag_items = request.session.get('bag_items', [])
        if subscription_plan_id not in bag_items:
            bag_items.append(subscription_plan_id)
            request.session['bag_items'] = bag_items
            messages.success(request, f"{subscription_plan} Subscription has been added to your Cart!") 
        else:
            messages.info(request, f"{subscription_plan} Subscription has been already added to your Cart!") 
        return redirect('get_started')



