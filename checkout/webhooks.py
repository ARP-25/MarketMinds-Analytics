from decimal import Decimal
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



# Webhook
@csrf_exempt
def stripe_webhook(request):
    """
    The primary endpoint for handling incoming Stripe webhook events.

    This function is the central processing point for all webhook events sent by Stripe 
    to the application. Upon receiving an event from Stripe, it first validates the 
    event's authenticity by verifying its signature against the STRIPE_WH_SECRET. This 
    ensures the event is indeed sent by Stripe and has not been tampered with during 
    transmission.

    After validation, the function dispatches the event to its respective handler 
    based on the event type. Each event type may have a dedicated handler function 
    designed to process the event and take necessary actions. If an event type does 
    not have a specific handler, it is directed to a default handler function 
    `handle_unexpected_event`.

    This webhook endpoint handles a variety of Stripe events including but not 
    limited to the creation of setup intents, creation and deletion of prices, 
    and changes to customer subscriptions. Each event type has logic specific to 
    the requirements and structure of that event.

    The following Stripe events are currently handled:
    - 'setup_intent.created': Handled by `handle_setup_intent_created`.
    - 'price.created': Handled by `handle_price_created`.
    - 'price.deleted': Handled by `handle_price_deleted`.
    - 'customer.subscription.created': Handled by `handle_subscription_created`.
    - 'customer.subscription.updated': Handled by `handle_subscription_updated`.
    - 'customer.subscription.deleted': Handled by `handle_subscription_deleted`.
    - Other unexpected events: Handled by `handle_unexpected_event`.

    Args:
    - request (HttpRequest): The Django HttpRequest object containing the webhook data 
      sent by Stripe.

    Returns:
    - HttpResponse: A Django HttpResponse object. Returns an HTTP status of 200 
      if the event is successfully processed, or 400 if there are any errors in event 
      validation or processing. This status is used by Stripe to confirm receipt of 
      the webhook event.

    Exceptions:
    - ValueError: Raised if the payload of the webhook is invalid. This could occur if 
      the payload is malformed or tampered with.
    - stripe.error.SignatureVerificationError: Raised if the event's signature does not 
      match the expected signature, indicating the event might not be from Stripe or 
      might have been altered.

    Note:
    - This endpoint is CSRF exempt, as it is intended to receive requests externally 
      from Stripe and not from the user's browser.
    - It is crucial to keep the Stripe API key and Webhook secret (`STRIPE_WH_SECRET`) 
      secure and not expose them in any logs or error messages.
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
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    event_handlers = {
        'setup_intent.created': handle_setup_intent_created,
        'price.created': handle_price_created,
        'price.deleted': handle_price_deleted,
        'customer.subscription.created': handle_subscription_created,
        'customer.subscription.updated': handle_subscription_updated,
        'customer.subscription.deleted': handle_subscription_deleted,
        'setup_intent.created': handle_setup_intent_created,
    }

    handler = event_handlers.get(event['type'], handle_unexpected_event)
    response = handler(event)
    return response if response else HttpResponse(status=200)


# Subscription Plan Creation Handling
def handle_price_created(event):
    """
    Handles the 'price.created' webhook event from Stripe.

    This function is triggered when a new price object is created in Stripe. The event data 
    is used to either create a new SubscriptionPlan or update an existing one in the Django 
    database, depending on the provided metadata.

    New Plan Creation:
    If the event's metadata indicates a new plan creation (add_action is true), a new 
    SubscriptionPlan object is created with details extracted from the metadata and Stripe's 
    price object.

    Existing Plan Update:
    If the metadata indicates an existing plan is being edited (edit_action is true), the 
    function first checks if there are any active subscriptions associated with this plan.
    - If active subscriptions are present, the plan is marked as 'unstaged' (i.e., not 
      directly editable). This ensures that changes to the plan do not affect active 
      subscribers.
    - If there are no active subscriptions, the plan is directly updated with new details 
      such as price, title, and description.

    Args:
    - event (dict): The Stripe event object containing webhook data. This includes all 
      information about the price creation, such as the price ID, metadata, and associated 
      product details.

    Returns:
    - HttpResponse: An HttpResponse object with a status code of 200. This indicates that 
      the event was received and processed successfully. In the case of an exception or 
      failure to find a matching SubscriptionPlan, appropriate error messages are printed, 
      but the function still returns an HttpResponse with a status code of 200 to acknowledge 
      receipt of the event to Stripe.

    Raises:
    - SubscriptionPlan.DoesNotExist: If the metadata references a Django plan ID that does 
      not exist in the database. This exception is caught within the function, and a message 
      is printed for logging purposes.

    Note:
    The function assumes that the price creation in Stripe includes relevant metadata for 
    plan creation or update. This metadata should ideally include identifiers and details 
    necessary to reflect the changes in the Django application's database.
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
    Handles the 'price.deleted' webhook event from Stripe.

    This function is triggered when a price associated with a subscription plan is 
    deleted in Stripe. The function looks up the corresponding SubscriptionPlan in 
    the Django database using the Stripe price ID obtained from the event's data.

    The function determines the appropriate action based on whether there are active 
    subscriptions linked to this plan:
    - If active subscriptions exist, the plan is marked as 'unstaged' by setting its 
      'staged' attribute to False. This action makes the plan inactive for new 
      subscriptions but retains it for existing subscribers, preserving their access.
    - If no active subscriptions are found, the plan is completely removed from the 
      database, effectively deleting the plan from the application's offerings.

    Args:
    - event (dict): The Stripe event object containing the data for the deleted price. 
      It includes the Stripe price ID and other relevant details of the deleted price.

    Returns:
    - HttpResponse: An HttpResponse object with a status code of 200, indicating the 
      successful processing of the webhook event. The function logs the outcome of the 
      processing, including whether the plan was marked as invisible or deleted.

    Exceptions:
    - SubscriptionPlan.DoesNotExist: This exception is raised if no SubscriptionPlan 
      is found with the given Stripe price ID. The exception is handled within the 
      function, and an informative message is logged.

    Note:
    - It is crucial to accurately handle the deletion of prices in Stripe to ensure 
      consistency between Stripe's records and the application's database.
    - This function is part of a series of webhook handlers that manage the synchronization 
      of Stripe events with the application's database, maintaining the integrity of 
      subscription-related data.
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

    This function is triggered when a new subscription is created on Stripe. It's responsible for
    creating a corresponding ActiveSubscription record in the Django application's database, syncing
    with Stripe's subscription data.

    The function extracts necessary data from the Stripe event, such as the user associated with
    the subscription, the price, and the plan. It then creates a new ActiveSubscription with this data.

    Args:
    - event (dict): The Stripe event object containing the webhook data. It includes details of the 
      created subscription, such as the customer ID, price ID, and plan details.

    Workflow:
    - Retrieves the user from the local database linked to the Stripe customer ID.
    - Retrieves price details from Stripe to calculate the monthly cost.
    - Fetches the corresponding SubscriptionPlan based on the Stripe price ID.
    - Creates a new ActiveSubscription instance with the retrieved data.

    Returns:
    - HttpResponse: A response with HTTP status 200 indicating successful handling of the event.

    Exceptions:
    - SubscriptionPlan.DoesNotExist: Occurs when no SubscriptionPlan with the given Stripe price ID
      is found in the database. In this case, no action is taken, but the incident should be logged
      for investigation.
    - Exception: Catches any other exceptions during the process. Ideally, exceptions should be logged
      to monitor any unexpected issues that occur.

    Notes:
    - The function assumes a one-to-one mapping between Stripe price IDs and SubscriptionPlans in the
      Django database.
    - The proper functioning of this handler is critical for keeping the application's subscription data
      in sync with Stripe's records.
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
        print(f"Subscription Plan not found for Stripe Price ID: {plan_stripe_id}")
        return HttpResponse("Subscription Plan not found", status=400)

    except Exception as e:       
        print(f"Error in handling subscription_created event: {e}")
        return HttpResponse("An error occurred", status=400)
        

    return HttpResponse(status=200)


# Renewal and Cancellation to a SPlan Handling
def handle_subscription_updated(event):
    """
    Handles the 'customer.subscription.updated' event from Stripe.

    This function processes updates to subscriptions in Stripe and synchronizes those changes
    with the ActiveSubscription records in the Django application's database. It's triggered when
    a subscription's status changes, such as renewals, cancellations, or other updates.

    The function updates the relevant ActiveSubscription instance's status, current period end date,
    and other relevant fields based on the data provided in the Stripe event.

    Args:
    - event (dict): The Stripe event object containing the updated subscription data. It includes the 
      updated status, the current period end timestamp, and whether the subscription is set to cancel 
      at the period end.

    Workflow:
    - Retrieves the ActiveSubscription from the database using the Stripe subscription ID from the event.
    - Updates the ActiveSubscription's status and current period end date.
    - If the subscription is set to cancel at the period end, the function also updates the canceled_at 
      and renewal_date fields, setting the status to 'pending cancellation'.
    - Saves the updated ActiveSubscription to the database.

    Returns:
    - HttpResponse: A response with HTTP status 200, indicating successful processing of the event.

    Exceptions:
    - ActiveSubscription.DoesNotExist: Raised if no ActiveSubscription is found with the provided Stripe 
      subscription ID. This is logged for audit purposes.
    - Exception: Catches any other unexpected exceptions during the process. These exceptions should be 
      logged for monitoring and debugging purposes.

    Notes:
    - It's essential to keep the ActiveSubscription data in the application's database in sync with Stripe 
      to ensure accurate and consistent subscription management.
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

    except ActiveSubscription.DoesNotExist:
        print(f"No active subscription found in the database with Stripe Subscription ID {subscription['id']}.")
    except Exception as e:
        print(f"Error in handle_subscription_updated: {e}")

    return HttpResponse(status=200)


# Deletion of a Subscription Handling from Stripe
# Internally we dont completely delete it, we just mark it as cancelled and expired
# so that we can keep the record of the subscription
# keeping user data for future analysis
def handle_subscription_deleted(event):
    """
    Handles the 'customer.subscription.deleted' webhook event from Stripe.

    This function is triggered when a subscription is deleted in Stripe. The deletion
    could be due to a cancellation or the end of a subscription period. This function 
    updates the corresponding ActiveSubscription record in the Django application's 
    database to reflect this change.

    The update includes setting the status of the ActiveSubscription to 'cancelled and expired' 
    and setting the current period end to None. This accurately reflects the state of the 
    subscription in the application, ensuring consistency with Stripe's records.

    Args:
    - event (dict): The Stripe event object containing the webhook data. It includes 
      the Stripe subscription ID and other relevant details of the deleted subscription.

    Workflow:
    - Retrieves the ActiveSubscription from the database using the Stripe subscription ID.
    - Updates the status of the ActiveSubscription to 'cancelled and expired'.
    - Sets the current period end date to None to indicate the end of the subscription.
    - Saves the changes to the ActiveSubscription record.

    Returns:
    - HttpResponse: A response with HTTP status 200, indicating successful processing of the event.

    Exceptions:
    - ActiveSubscription.DoesNotExist: Raised if no ActiveSubscription is found with the 
      provided Stripe subscription ID. This situation is logged for investigation purposes.
    - Exception: Catches any other exceptions that occur during processing. Such exceptions 
      should be logged to facilitate debugging and monitoring of the webhook handling.

    Notes:
    - Handling this event accurately is crucial for maintaining the integrity of subscription 
      data within the application.
    """
    subscription = event['data']['object']
    stripe_subscription_id = subscription['id']

    try:
        active_subscription = ActiveSubscription.objects.get(stripe_subscription_id=stripe_subscription_id)
        active_subscription.status = 'cancelled and expired'
        active_subscription.current_period_end = None
        active_subscription.save()
        print(f"Updated subscription status to 'cancelled and expired' for {stripe_subscription_id}")
    except ActiveSubscription.DoesNotExist:
        print(f"No active subscription found in the database with Stripe Subscription ID {stripe_subscription_id}.")
    except Exception as e:
        print(f"Error in handle_subscription_deleted: {e}")

    return HttpResponse(status=200)


# Default Event Handling
def handle_unexpected_event(event):
    """
    Handles any unexpected or unhandled Stripe webhook events.

    This function acts as a catch-all for Stripe events that do not match any of the 
    predefined event types in the webhook handling system. It is essential for logging 
    and acknowledging the receipt of these unexpected events. This helps maintain the 
    integrity of the webhook processing system by ensuring that all events sent by Stripe 
    are received and noted, even if they are not explicitly handled.

    While this function does not process the event data, logging these events is crucial 
    for identifying potential updates or changes in Stripe's API or new event types that 
    may require handling in future updates of the application.

    Args:
    - event (dict): The Stripe event object containing the webhook data. It includes the
      type of the event and other relevant details.

    Returns:
    - HttpResponse: A response with HTTP status 200, indicating that the event was received
      but not processed due to it being unexpected or not fitting into the predefined event types.

    Note:
    - It's advisable to regularly review the logs of unexpected events to keep the application's
      webhook handling system up to date with any changes or additions in Stripe's webhook events.
    """
    print(f"Unerwartetes Event erhalten: {event['type']}")
    return HttpResponse(status=200)


# Not needed for now since it is implicitly handled within stripe subscription process.
# In later iteration of the program potential use case could be to handle the setup intent creation 
# for different products than subscriptions.
def handle_setup_intent_created(event):
    """
    Placeholder function for handling 'setup_intent.created' Stripe webhook events.

    Currently, this function does not perform any specific actions. It serves as a placeholder
    in the webhook handling system for the 'setup_intent.created' event. The setup intent creation 
    process is managed implicitly by Stripe, particularly in the context of setting up subscriptions 
    or other payment methods.

    In future iterations of the application, this function could be expanded to handle more 
    complex scenarios, such as creating setup intents for different types of products beyond 
    the standard subscription models, or implementing custom logic during the setup intent creation.

    Args:
    - event (dict): The Stripe event object containing the webhook data related to the setup 
      intent creation. It includes details such as the setup intent ID and associated customer 
      information.

    Returns:
    - HttpResponse: A response with HTTP status 200, indicating the receipt of the event. 
      As the function currently does not process the event, this serves as an acknowledgment 
      to Stripe that the event was received.

    Note:
    - Keeping this function in the webhook handling system ensures that all types of events 
      sent by Stripe are acknowledged, maintaining the integrity of the webhook processing 
      system.
    - Future developments may leverage this function to implement more specific behaviors 
      tailored to the application's evolving requirements.
    """
    return HttpResponse(status=200)


# Helper Functions
def get_user_from_stripe_customer_id(customer_id):
    """
    Retrieves the User object associated with a given Stripe customer ID.

    This function queries the application's database to find the UserProfile that matches
    the provided Stripe customer ID. It is used to link Stripe's customer-related data with 
    the corresponding user in the Django application. This linkage is crucial for operations 
    that require correlating Stripe customers with application users, such as handling 
    subscription events or processing payments.

    Args:
    - customer_id (str): The Stripe customer ID associated with a user's profile.

    Returns:
    - User: The Django User object linked to the given Stripe customer ID, if found.
    - None: If no matching UserProfile is found in the database.

    Raises:
    - No specific exceptions are raised by this function. It handles the UserProfile.DoesNotExist 
      exception internally and returns None in case of no matching record.

    Notes:
    - The function assumes that there is a one-to-one mapping between Stripe customer IDs and 
      UserProfiles in the application's database.
    - In a production environment, consider replacing the print statement with proper logging 
      for better error tracking and diagnostics.
    """
    try:
        user_profile = UserProfile.objects.get(stripe_customer_id=customer_id)
        return user_profile.user  
    except UserProfile.DoesNotExist:
        print(f"No UserProfile found for Stripe Customer ID {customer_id}")
        return None
