from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.utils import timezone

import stripe
import json
from datetime import datetime, timedelta

from bag.contexts import bag_contents
from subscription.models import SubscriptionPlan
from .forms import ActiveSubscriptionForm  
from profiles.forms import UserProfileForm
from profiles.models import UserProfile


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    Handles the checkout process for subscriptions.

    Args:
        request: The HTTP request object.

    Returns:
        Renders the checkout page and processes subscription payments.
        If successful, renders 'checkout_success.html' after subscription creation.
    """
    bag = request.session.get('bag_items', [])
    if not bag:
        messages.error(request, 'There\'s nothing in your bag at the moment')
    if request.user.is_authenticated:
        if request.method == 'POST':
            for plan_id in bag:
                subscription_plan = get_object_or_404(SubscriptionPlan, id=plan_id)
                active_subscription_form = ActiveSubscriptionForm(request.POST)
                if active_subscription_form.is_valid():
                    subscription = active_subscription_form.save(commit=False)
                    subscription.user = request.user
                    subscription.subscription_plan = subscription_plan
                    subscription.end_date = timezone.now() + timedelta(days=30)
                    subscription.save()
                    messages.success(request, f'Thank you for subscribing to {subscription_plan.title}!')                   
                    if 'save-info' in request.POST:                    
                        user_profile = UserProfile.objects.get(user=request.user)
                        data_from_form = active_subscription_form.cleaned_data
                        form_fields = data_from_form.keys()
                        for field in form_fields:
                            if hasattr(user_profile, field):
                                setattr(user_profile, field, data_from_form[field])
                        user_profile.save()   
                    if 'bag_items' in request.session:
                        del request.session['bag_items']

            return render(request, 'checkout/checkout_success.html')

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
