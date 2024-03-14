from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.utils import timezone
from django.core.mail import send_mail


import stripe
import json
from datetime import datetime, timedelta

from bag.contexts import bag_contents
from subscription.models import SubscriptionPlan
from .models import ActiveSubscription
from .forms import ActiveSubscriptionForm  
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from .email_utils import send_subscription_confirmation_email




def checkout_adjust(request, item_id):
    """
    View function to adjust the contents of the shopping bag during checkout.

    Args:
    - request: HTTP request object.
    - item_id: ID of the subscription plan to adjust.

    Returns:
    - Redirects to the 'checkout' page or 'get_started' page after adjusting the shopping bag.
    """
    bag_items = request.session.get('bag_items', [])
    subscription_plan = get_object_or_404(SubscriptionPlan, pk=item_id)

    if str(item_id) in bag_items:
        bag_items.remove(str(item_id))
        messages.success(request, f"{subscription_plan} successfully removed from your bag!")
    else:
        messages.error(request, "The item was not in your bag.")

    request.session['bag_items'] = bag_items

   
    if not bag_items:
        messages.info(request, "Your bag is empty. Add subscription plans to proceed with checkout.")
        return redirect('get_started')  

    return redirect('checkout')


def checkout_success(request):
    """
    View function for handling the post-checkout success scenario.

    This function is triggered when a user successfully completes a checkout. It
    performs two main tasks: sending a subscription confirmation email and rendering
    the checkout success page. The function first calls 'send_subscription_confirmation_email'
    to send an email with details of the user's active subscriptions. It then clears
    the 'bag_items' from the session to reset the shopping bag. Finally, it renders
    the checkout success page to confirm the successful transaction to the user.

    Args:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: A rendered checkout success page, confirming the successful transaction.
    """
    send_subscription_confirmation_email(request)
    request.session.pop('bag_items', None)

    return render (request, 'checkout/checkout_success.html')


def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    template = 'checkout/checkout.html'

    if request.method == 'POST':
        active_subscription_form = ActiveSubscriptionForm(request.POST)
        bag = request.session.get('bag_items', [])
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('view_bag'))

        if not active_subscription_form.is_valid():
            messages.error(request, "There was an error with the form. Please check your information.")
            return render(request, template, {'active_subscription_form': active_subscription_form})

        payment_method_id = request.POST.get('payment_method_id')
        if not payment_method_id:
            messages.error(request, "No payment method provided.")
            return render(request, template, {'active_subscription_form': active_subscription_form})

        customer_id = get_or_create_stripe_customer(request.user)

        # Ensure that customer_id is a string (the ID of the customer)
        if isinstance(customer_id, stripe.Customer):
            customer_id = customer_id.id

        for plan_id in bag:
            subscription_plan = get_object_or_404(SubscriptionPlan, id=plan_id)

            # Prüfen, ob eine aktive Subscription existiert
            if ActiveSubscription.objects.filter(
                user=request.user, 
                subscription_plan=subscription_plan
            ).exists():
                messages.error(request, f"You already have an active subscription for {subscription_plan.title}.")
                continue   
            try:
                stripe.PaymentMethod.attach(payment_method_id, customer=customer_id)
                stripe.Customer.modify(customer_id, invoice_settings={'default_payment_method': payment_method_id})
                stripe.Subscription.create(customer=customer_id, items=[{"plan": subscription_plan.stripe_price_id}])

                stripe_subscription = stripe.Subscription.create(
                    customer=customer_id,
                    items=[{"plan": subscription_plan.stripe_price_id}],
                )

                # Save the subscription info in ActiveSubscription model
                active_subscription = ActiveSubscription(
                    user=request.user,
                    subscription_plan=subscription_plan,
                    stripe_subscription_id=stripe_subscription.id,  # Save Stripe Subscription ID
                    status=stripe_subscription.status,  # Save Stripe Subscription Status
                )
                active_subscription.save()

            except stripe.error.StripeError as e:
                messages.error(request, "Stripe Error: " + str(e))
                continue  # Springt zum nächsten Plan in der Schleife

        if not ActiveSubscription.objects.filter(user=request.user, subscription_plan__in=bag, status='active').exists():
            messages.error(request, "Keine neuen Abonnements erstellt.")
            return redirect(reverse('bag'))

        messages.success(request, "Thank you for your subscription!")
        return redirect('checkout_success')

    else:
        active_subscription_form = ActiveSubscriptionForm()
        setup_intent = stripe.SetupIntent.create()

        active_subscription_plan_id_user = []
        if request.user.is_authenticated:
            active_subscriptions = ActiveSubscription.objects.filter(user=request.user).values_list('subscription_plan_id', flat=True)
            active_subscription_plan_id_user = list(map(str, active_subscriptions))

        context = {
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
            'client_secret': setup_intent.client_secret,
            'active_subscription_form': active_subscription_form,
            'active_subscription_plan_id_user': active_subscription_plan_id_user
        }
        return render(request, template, context)


def get_or_create_stripe_customer(user):
    # Assuming you have a UserProfile model linked to your User model
    profile = UserProfile.objects.get(user=user)

    # Check if the user already has a Stripe customer ID
    if profile.stripe_customer_id:
        try:
            # Retrieve existing Stripe customer
            return stripe.Customer.retrieve(profile.stripe_customer_id)
        except stripe.error.StripeError:
            # Handle error (e.g., customer not found)
            pass

    # If not, create a new Stripe customer
    try:
        customer = stripe.Customer.create(
            email=user.email,
            metadata={'user_id': user.id}
        )
        # Save the Stripe customer ID in your UserProfile model
        profile.stripe_customer_id = customer.id
        profile.save()
        return customer
    except stripe.error.StripeError as e:
        # Handle error
        print(f"Stripe error: {e}")
        return None
