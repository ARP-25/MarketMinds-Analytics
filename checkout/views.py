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


def get_or_create_stripe_customer(user):
    """
    Retrieves an existing Stripe customer or creates a new one for the given user.

    This function first checks if the user already has a linked Stripe customer 
    (identified by a Stripe customer ID stored in the user's profile). If a Stripe 
    customer ID exists, the function attempts to retrieve the corresponding customer 
    from Stripe. If the user does not have a linked Stripe customer or if the 
    retrieval fails, the function proceeds to create a new Stripe customer.

    The process of creating a new Stripe customer involves calling the Stripe API to 
    create a customer object with the user's email and a metadata field containing the 
    user's ID. The newly created Stripe customer ID is then stored in the user's profile.

    Args:
    - user (User): The Django User instance for whom the Stripe customer is to be 
      retrieved or created.

    Returns:
    - stripe.Customer or None: Returns the Stripe Customer object if the customer is 
      successfully retrieved or created. Returns None if an error occurs during the 
      process.

    Raises:
    - stripe.error.StripeError: This exception is raised if any Stripe API call fails.
      The function handles these exceptions by logging the error and returning None.

    Notes:
    - It's important to handle Stripe API exceptions to prevent the application from 
      crashing due to external API failures.
    - The function assumes the existence of a UserProfile model linked to the User 
      model, storing the Stripe customer ID.
    """
    profile = UserProfile.objects.get(user=user)
    if profile.stripe_customer_id:
        try:
            return stripe.Customer.retrieve(profile.stripe_customer_id)
        except stripe.error.StripeError:
            pass
    try:
        customer = stripe.Customer.create(
            email=user.email,
            metadata={'user_id': user.id}
        )
        profile.stripe_customer_id = customer.id
        profile.save()
        return customer
    except stripe.error.StripeError as e:
        print(f"Stripe error: {e}")
        return None


def process_or_renew_subscription(request, customer_id, payment_method_id, subscription_plan):
    """
    Processes a new subscription or renews an existing one based on the given parameters.

    This function either renews a subscription that's marked as 'pending cancellation' or 
    creates a new subscription if no such existing subscription is found. It interacts with 
    Stripe to modify or create the subscription accordingly.

    For renewing a subscription:
    - It looks for an existing ActiveSubscription with a status of 'pending cancellation'.
    - If found, it sends a request to Stripe to renew this subscription by updating its
      details and resetting the cancellation at period end.

    For creating a new subscription:
    - It attaches the provided payment method to the customer and sets it as the default payment method.
    - Then, it creates a new subscription in Stripe with the specified plan.

    In both cases, success or error messages are communicated back to the user through Django's 
    messaging framework. The actual update or creation of the ActiveSubscription object in the 
    database is handled by a Stripe webhook, not within this function.

    Args:
    - request (HttpRequest): The request object, used for accessing user information and sending messages.
    - customer_id (str): The Stripe customer ID for the user.
    - payment_method_id (str): The Stripe payment method ID to be used for the subscription.
    - subscription_plan (SubscriptionPlan): The SubscriptionPlan object representing the plan to subscribe to.

    Returns:
    - bool: True if the subscription process (renewal or creation) is initiated successfully, False otherwise.

    Raises:
    - stripe.error.StripeError: If any Stripe API call within the function fails. This exception 
      is caught, and an appropriate error message is sent to the user.
    """
    existing_subscription = ActiveSubscription.objects.filter(
        user=request.user, 
        subscription_plan=subscription_plan,
        status='pending cancellation'
    ).first()

    if existing_subscription:
        try:
            stripe.Subscription.modify(
                existing_subscription.stripe_subscription_id,
                cancel_at_period_end=False,
                items=[{"id": stripe.Subscription.retrieve(existing_subscription.stripe_subscription_id)['items']['data'][0]['id'], "plan": subscription_plan.stripe_price_id}],
            )
            messages.success(request, f"{subscription_plan.title} subscription renewal initiated successfully.")
            return True
        except stripe.error.StripeError as e:
            messages.error(request, "Stripe Error: " + str(e))
            return False
    else:
        try:
            stripe.PaymentMethod.attach(payment_method_id, customer=customer_id)
            stripe.Customer.modify(customer_id, invoice_settings={'default_payment_method': payment_method_id})
            stripe.Subscription.create(
                customer=customer_id,
                items=[{"plan": subscription_plan.stripe_price_id}],
            )
            messages.success(request, f"{subscription_plan.title} subscription creation initiated successfully.")
            return True
        except stripe.error.StripeError as e:
            messages.error(request, "Stripe Error: " + str(e))
            return False


def process_checkout(request, bag, payment_method_id, customer_id):
    """
    Processes the checkout for multiple subscription plans.

    This function iterates through a list of subscription plan IDs, typically obtained 
    from a user's shopping bag or cart, and processes each one either by renewing an 
    existing subscription or creating a new one.

    For each plan ID in the bag:
    - The function first checks if the user already has an active subscription for the 
      given plan. If so, an error message is displayed, and the function skips to the 
      next plan.
    - If the user does not have an active subscription for that plan, the function 
      attempts to process or renew the subscription through `process_or_renew_subscription`.

    Args:
    - request (HttpRequest): The HttpRequest object, used to access user information and 
      to pass messages back to the frontend.
    - bag (list): A list of subscription plan IDs representing the user's selected subscription plans.
    - payment_method_id (str): The Stripe payment method ID to be used for the subscriptions.
    - customer_id (str): The Stripe customer ID associated with the user.

    Returns:
    - bool: Returns True if all subscriptions in the bag are processed successfully. 
      Returns False if any subscription process fails, stopping further processing.

    Notes:
    - This function is essential for handling bulk subscription purchases or renewals.
    - The function delegates the actual processing of each subscription to 
      `process_or_renew_subscription`, allowing for a clear separation of concerns.
    - In case of a failure in processing any subscription, the function halts and returns 
      False to prevent partial subscription processing.
    """
    for plan_id in bag:
        subscription_plan = get_object_or_404(SubscriptionPlan, id=plan_id)
        if ActiveSubscription.objects.filter(
            user=request.user, 
            subscription_plan=subscription_plan,
            status__in=['active']
        ).exists():
            messages.error(request, f"You already have an active subscription for {subscription_plan.title}.")
            continue
        success = process_or_renew_subscription(request, customer_id, payment_method_id, subscription_plan)
        if not success:
            return False
    return True


def checkout(request):
    """
    Handles the checkout process for purchasing subscription plans.

    This view function manages the checkout process when a user decides to purchase one 
    or more subscription plans. It involves several key steps, including form validation, 
    Stripe payment processing, and subscription management. The function caters to both 
    POST requests (processing the checkout) and GET requests (displaying the checkout form).

    Workflow for POST requests:
    - Validates the user's bag items and the submitted subscription form.
    - Creates or retrieves a Stripe customer based on the user's data.
    - Processes the payment and subscription creation through Stripe.
    - Redirects to the success page upon successful payment and subscription.

    Workflow for GET requests:
    - Prepares the subscription form and setup intent for Stripe's payment interface.
    - Retrieves any active subscriptions of the user to prevent duplicate purchases.
    - Renders the checkout page with the necessary context data.

    Args:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: Renders the checkout page on GET request or redirects to another page 
      based on the outcome of the checkout process on POST request.

    Notes:
    - Stripe API keys and client secrets are handled within this function for payment processing.
    - Error messages and redirections are used to handle different scenarios like form errors, 
      empty bag, or payment issues.
    - The function assumes the presence of 'bag_items' in the session to retrieve the user's 
      selected subscription plans.
    """
    stripe.api_key = settings.STRIPE_SECRET_KEY
    template = 'checkout/checkout.html'
    bag = request.session.get('bag_items', [])

    if request.method == 'POST':
        active_subscription_form = ActiveSubscriptionForm(request.POST)      
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment.")
            return redirect(reverse('view_bag'))
        
        if not active_subscription_form.is_valid():
            messages.error(request, "There was an error with the form. Please check your information.")
            return render(request, template, {'active_subscription_form': active_subscription_form})
        
        payment_method_id = request.POST.get('payment_method_id')
        if not payment_method_id:
            messages.error(request, "No payment method provided.")
            return render(request, template, {'active_subscription_form': active_subscription_form})
        
        customer = get_or_create_stripe_customer(request.user)
        customer_id = customer.id if isinstance(customer, stripe.Customer) else customer
        if not process_checkout(request, bag, payment_method_id, customer_id):
            return redirect(reverse('bag'))
        
        messages.success(request, "Thank you for your subscription!")
        return redirect('checkout_success')
    
    else:
        active_subscription_form = ActiveSubscriptionForm()
        setup_intent = stripe.SetupIntent.create()
        active_subscription_plan_id_user = []

        if request.user.is_authenticated:
            active_subscriptions = ActiveSubscription.objects.filter(
                user=request.user, 
                canceled_at__isnull=True
            ).values_list('subscription_plan_id', flat=True)
            active_subscription_plan_id_user = list(map(str, active_subscriptions))

        context = {
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
            'client_secret': setup_intent.client_secret,
            'active_subscription_form': active_subscription_form,
            'active_subscription_plan_id_user': active_subscription_plan_id_user
        }
        return render(request, template, context)

