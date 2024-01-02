from django.shortcuts import render, redirect
from subscription.models import SubscriptionPlan

def bag(request):
    """
    A View to return bag page
    """
    # Test if the session bag
    print(request.session.get('bag_items', []))  

    return render(request, 'bag/bag.html')


def add_to_bag(request):
    # Fetching subscription_plan_id from the Request Obj
    subscription_plan_id = int(request.POST.get('subscription_plan_id'))

    # Fetching redirect_url from the Request Obj
    redirect_url = request.POST.get('redirect_url')

    # Fetching bag_items from session
    bag_items = request.session.get('bag_items', [])

    # Add Subscription Plan ID to the bag or notify already added
    if subscription_plan_id in bag_items:
        print("You already successfully added this Subscription Plan to your Bag")
    else:
        # Add subscription_plan_id to bag_items       
        bag_items.append(subscription_plan_id)
        request.session['bag_items'] = bag_items  # Aktualisiere session

    # Test if Subscription Plan Id got added to the session bag
    print(request.session.get('bag_items', []))  

    return redirect(redirect_url)