from decimal import Decimal
import logging
from django.utils import timezone
from datetime import datetime

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import ActiveSubscription
from profiles.models import UserProfile
from subscription.models import SubscriptionPlan


import stripe

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Webhook
@csrf_exempt
def stripe_webhook(request):
    """
    The primary webhook endpoint for handling Stripe events.

    This function is the entry point for all webhook events sent by Stripe to the 
    application. It validates the event by verifying its signature using the 
    STRIPE_WH_SECRET, ensuring it's a legitimate event sent by Stripe.

    Depending on the type of the event received from Stripe, it delegates the handling 
    to specific functions designed for each event type. If an event type does not 
    have a dedicated handler, it defaults to using `handle_unexpected_event` to 
    process the event.

    Currently, it handles the following Stripe events:
    - 'setup_intent.created': Calls the function to handle setup intent creation.
    - 'price.deleted': Calls the function to handle the deletion of a price.

    Args:
    - request: The HTTP request object from Django containing the webhook data.

    Returns:
    - HttpResponse: A response with HTTP status 200 for successful processing, or 
      400 for any errors encountered during the event validation or processing.
    """   

    stripe.api_key = settings.STRIPE_SECRET_KEY
    wh_secret = settings.STRIPE_WH_SECRET

    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')


    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        #log
        logger.error(f"Webhook error: Invalid payload - {e}")
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        #log
        logger.error(f"Webhook error: Invalid signature - {e}")
        return HttpResponse(status=400)

    #log
    logger.debug(f"Received Stripe webhook event: {event['type']}")

    event_handlers = {
        'setup_intent.created': handle_setup_intent_created,
        'price.created': handle_price_created,
        'price.deleted': handle_price_deleted,
        'customer.subscription.created': handle_subscription_created,
        'customer.subscription.updated': handle_subscription_updated,
        'setup_intent.created': handle_setup_intent_created,
    }

    handler = event_handlers.get(event['type'], handle_unexpected_event)
    response = handler(event)
    return response if response else HttpResponse(status=200)


# Subscription Plan Creation Handling
def handle_price_created(event):
    """
    Handles the 'price.created' webhook event from Stripe. This function is invoked when a new price is created in Stripe.
    It checks whether the new price corresponds to a new plan creation or an edit of an existing plan.

    For a new plan creation:
    - Creates a new SubscriptionPlan object in the Django database using the metadata from Stripe.

    For an existing plan edit:
    - Checks for active subscriptions associated with this plan.
    - If active subscriptions exist, the plan is marked as 'unstaged' and not directly edited.
    - If there are no active subscriptions, updates the existing plan with new details.
    
    Args:
    - event: The Stripe event object containing webhook data.

    Returns:
    - HttpResponse with a status code indicating the result of the operation.
    """
    price = event['data']['object']
    metadata = price['metadata']

    if 'edit_action' in metadata and metadata['edit_action'] == 'true':
        django_plan_id = metadata['django_plan_id']

        try:
            subscription_plan = SubscriptionPlan.objects.get(id=django_plan_id)
            if ActiveSubscription.objects.filter(subscription_plan=subscription_plan).exists():
                # Mark the existing plan as 'unstaged' instead of directly editing it
                subscription_plan.staged = False
                subscription_plan.save()
                print(f"Plan {subscription_plan.title} marked as inactive due to active subscriptions.")
            else:
                # Update the plan directly as there are no active subscriptions
                subscription_plan.stripe_price_id = price['id']
                subscription_plan.price = metadata.get('price', subscription_plan.price)
                subscription_plan.title = metadata.get('title', subscription_plan.title)
                subscription_plan.description = metadata.get('description', subscription_plan.description)
                subscription_plan.save()
        except SubscriptionPlan.DoesNotExist:
            print(f"No SubscriptionPlan found with ID {django_plan_id} in the database.")

    elif 'add_action' in metadata and metadata['add_action'] == 'true':
        if not SubscriptionPlan.objects.filter(stripe_price_id=price['id']).exists():
            SubscriptionPlan.objects.create(
                title=metadata['title'],
                description=metadata['description'],
                price=metadata.get('price', 0.00),
                image=metadata.get('image_url', ''),
                stripe_price_id=price['id']
            )

    return HttpResponse(status=200)


# Subscription Plan Deletion Handling
def handle_price_deleted(event):
    """
    Handles the 'price.deleted' event from Stripe webhooks.

    This function is called when a price is deleted in Stripe. It looks up the 
    corresponding SubscriptionPlan in the Django database using the Stripe price ID 
    from the event data. If the plan is found, the function checks whether any active 
    subscriptions are associated with this plan.

    - If there are active subscriptions linked to the plan, the plan is not deleted 
      from the database. Instead, it is marked as invisible ('staged' is set to False) 
      to prevent it from being used for new subscriptions but retains it for the sake 
      of existing subscribers.
    
    - If there are no active subscriptions linked to the plan, it is safe to remove 
      the plan entirely from the database.

    Args:
    - event: The Stripe event object containing the data for the deleted price.

    Returns:
    - HttpResponse: A response with HTTP status 200, indicating successful handling of the event.
    """
    deleted_price = event['data']['object']
    stripe_price_id = deleted_price['id']

    try:
        subscription_plan = SubscriptionPlan.objects.get(stripe_price_id=stripe_price_id)
        if ActiveSubscription.objects.filter(subscription_plan=subscription_plan).exists():
            subscription_plan.staged = False
            subscription_plan.save()
            print(f"Plan {subscription_plan.title} has been marked as invisible due to active subscriptions.")
        else:
            subscription_plan.delete()
            print(f"Subscription Plan {subscription_plan.title} deleted.")
    except SubscriptionPlan.DoesNotExist:
        print(f"No plan found in the database with Stripe Price ID {stripe_price_id}.")
    
    return HttpResponse(status=200)


# Subscribing to a Plan Handling
def handle_subscription_created(event):
    """
    Handles the 'customer.subscription.created' event from Stripe.
    """
    subscription = event['data']['object']
    user = get_user_from_stripe_customer_id(subscription['customer'])
    price_id = subscription["items"]["data"][0]["price"]["id"]
    plan_stripe_id = subscription['plan']['id']

    try:
        price_details = stripe.Price.retrieve(price_id)
        monthly_cost = Decimal(price_details["unit_amount"]) / 100
        subscription_plan = SubscriptionPlan.objects.get(stripe_price_id=plan_stripe_id)       
        new_active_subscription = ActiveSubscription.objects.create(
            user=user,
            subscription_plan=subscription_plan,  
            stripe_subscription_id=subscription['id'],
            status=subscription['status'],
            current_period_end=timezone.make_aware(
                datetime.fromtimestamp(subscription['current_period_end'])
            ),
            renewal_date=timezone.make_aware(
                datetime.fromtimestamp(subscription['current_period_end'])
            ),
            monthly_cost=monthly_cost
        )
        new_active_subscription.save()

    except SubscriptionPlan.DoesNotExist:
        logger.error(f"No SubscriptionPlan found with Stripe Price ID {plan_stripe_id}")
    except Exception as e:
        logger.error(f"Error in handling subscription_created event: {e}")

    return HttpResponse(status=200)


# Renewal and Cancellation to a SPlan Handling
def handle_subscription_updated(event):
    """
    Handles the 'customer.subscription.updated' event from Stripe.

    Args:
    - event: The Stripe event object containing webhook data.

    Returns:
    - HttpResponse with a status code indicating the result of the operation.
    """
    subscription = event['data']['object']

    try:
        active_subscription = ActiveSubscription.objects.get(stripe_subscription_id=subscription['id'])
        active_subscription.status = subscription['status']
        active_subscription.current_period_end = timezone.make_aware(
            datetime.fromtimestamp(subscription['current_period_end'])
        )
        if subscription['cancel_at_period_end']:
            active_subscription.canceled_at = timezone.make_aware(
                datetime.fromtimestamp(subscription['canceled_at'])
            )
            active_subscription.renewal_date = None                        
            active_subscription.status = 'pending cancellation'
        else:
            active_subscription.renewal_date = active_subscription.current_period_end
            active_subscription.canceled_at = None
        active_subscription.save()
        print(f"Updated subscription: {active_subscription}")
    except ActiveSubscription.DoesNotExist:
        print(f"No active subscription found in the database with Stripe Subscription ID {subscription['id']}.")

    return HttpResponse(status=200)


# Default Event Handling
def handle_unexpected_event(event):
    print(f"Unerwartetes Event erhalten: {event['type']}")
    return HttpResponse(status=200)


# Not needed for now since it is implicitly handled within stripe subscription process.
# In later iteration of the program potential use case could be to handle the setup intent creation 
# for different products than subscriptions.
def handle_setup_intent_created(event):
    
    return HttpResponse(status=200)


# Helper Functions
def get_user_from_stripe_customer_id(customer_id):
    """
    Helper function to get the user associated with a Stripe customer ID.
    """
    try:
        user_profile = UserProfile.objects.get(stripe_customer_id=customer_id)
        return user_profile.user  
    except UserProfile.DoesNotExist:
        logger.error(f"No UserProfile found for Stripe Customer ID {customer_id}")
        return None
