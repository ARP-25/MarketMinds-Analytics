import json
import stripe
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.contrib.auth.models import User
from .models import ActiveSubscription, SubscriptionPlan

from django.conf import settings
stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def stripe_webhook_handler(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Process the Stripe webhook event
    if event['type'] == 'invoice.payment_succeeded':
        invoice = event['data']['object']
        subscription_id = invoice.get('subscription')
        amount_paid = invoice.get('total')  # total amount in cents
        if subscription_id:
            try:
                stripe_subscription = stripe.Subscription.retrieve(subscription_id)
                customer_id = stripe_subscription.customer
                customer = stripe.Customer.retrieve(customer_id)
                
                # Extract user_id from Stripe customer metadata
                user_id = customer.metadata.get('user_id')
                if user_id:
                    user = User.objects.get(id=user_id)

                    # Find or create the ActiveSubscription
                    active_subscription, created = ActiveSubscription.objects.get_or_create(
                        user=user,
                        stripe_subscription_id=subscription_id,
                        defaults={
                            'subscription_plan': get_plan_from_stripe_id(stripe_subscription.plan.id),
                        }
                    )

                    active_subscription.start_date = timezone.now()
                    active_subscription.renewal_date = active_subscription.start_date + timezone.timedelta(days=30)
                    active_subscription.billing_amount = amount_paid / 100  # Convert to standard currency format
                    active_subscription.save()

            except (ActiveSubscription.DoesNotExist, User.DoesNotExist, stripe.error.StripeError) as e:
                # Handle exceptions
                print(f"Webhook handler error: {e}")
                
    if event['type'] == 'customer.subscription.deleted':
        subscription = event['data']['object']
        subscription_id = subscription['id']
        try:
            active_subscription = ActiveSubscription.objects.get(stripe_subscription_id=subscription_id)
            active_subscription.delete()

        except ActiveSubscription.DoesNotExist:

            pass

    # Add handlers for other webhook events as necessary

    return HttpResponse(status=200)


def get_plan_from_stripe_id(stripe_plan_id):
    try:
        return SubscriptionPlan.objects.get(stripe_plan_id=stripe_plan_id)
    except SubscriptionPlan.DoesNotExist:
        # Logging this situation as it's unusual
        print(f"Plan with Stripe ID {stripe_plan_id} not found in the database.")
        return None
