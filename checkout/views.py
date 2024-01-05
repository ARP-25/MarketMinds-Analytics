from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

import stripe
from datetime import datetime, timedelta

from bag.contexts import bag_contents
from subscription.models import SubscriptionPlan
from .forms import ActiveSubscriptionForm  


def checkout(request):
    # Getting bag_items
    bag = request.session.get('bag_items', [])
    if not bag:
        messages.error(request, 'There\'s nothing in your bag at the moment')

    # Handle Create or Update ActiveSubscription and associate ActiveSubscription with User:
    if request.method == 'POST':
        for plan_id in bag:
            subscription_plan = get_object_or_404(SubscriptionPlan, id=plan_id)
            active_subscription_form = ActiveSubscriptionForm(request.POST)
            if active_subscription_form.is_valid():
                subscription = active_subscription_form.save(commit=False)
                subscription.user = request.user
                subscription.subscription_plan = subscription_plan
                subscription.end_date = datetime.now() + timedelta(days=30)
                subscription.save()
                messages.success(request, f'Thank you for subscribing to {subscription_plan.title}!')
        return redirect(reverse('checkout'))

    # Render Template and handle Stripe Payment 
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    current_bag = bag_contents(request)
    total = current_bag['total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    if not stripe_public_key:
        message.warning(request, 'Stripe public key is missing. Did you forget to set it in your environment?')

    active_subscription_form = ActiveSubscriptionForm()  
    template = 'checkout/checkout.html'
    context = {
        'active_subscription_form': active_subscription_form,  
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)
