from django.shortcuts import render, redirect
from subscription.models import SubscriptionPlan
from django.contrib import messages

def bag(request):
    """
    A View to return bag page
    """
    print(request.session.get('bag_items', []))  

    return render(request, 'bag/bag.html')


def add_to_bag(request):
    subscription_plan_id = int(request.POST.get('subscription_plan_id'))
    redirect_url = request.POST.get('redirect_url')
    bag_items = request.session.get('bag_items', [])
    if subscription_plan_id in bag_items:
        messages.info(request, "You already successfully added this Subscription Plan to your Cart.")
    else:       
        bag_items.append(subscription_plan_id)
        request.session['bag_items'] = bag_items  
        messages.success(request, "Successfully added Subscription Plan to your Cart.")
    print(request.session.get('bag_items', []))  

    return redirect(redirect_url)


