from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib import messages

from .models import ActiveSubscription
from subscription.models import SubscriptionPlan
from .forms import ActiveSubscriptionForm

from datetime import datetime, timedelta
import json
import time

class StripeWH_Handler:
    """
    Handle Stripe webhooks.

    Attributes:
        request (HttpRequest): The HTTP request object.

    Methods:
        handle_event(event): Handle a generic/unknown/unexpected webhook event.
        handle_payment_intent_succeeded(event): Handle the payment_intent.succeeded webhook from Stripe.
        handle_payment_intent_payment_failed(event): Handle the payment_intent.payment_failed webhook from Stripe.
    """

    def __init__(self, request):
        """
        Initialize the Stripe Webhook Handler.

        Args:
            request (HttpRequest): The HTTP request object.
        """
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event.

        Args:
            event (dict): The webhook event data.

        Returns:
            HttpResponse: The HTTP response indicating the handling of the webhook event.
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)



    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe.
        Create ActiveSubscription when checkout View fails to do so.

        Args:
            event (dict): The webhook event data.

        Returns:
            HttpResponse: The HTTP response indicating the handling of the webhook event.
        """
        intent = event.data.object
        bag_items = json.loads(intent.metadata.bag)
        user_name = intent.metadata.username

        try:
            user = User.objects.get(username=user_name)
            subscription_plan_ids = list(map(str, ActiveSubscription.objects.filter(user=user.id).values_list('subscription_plan__id', flat=True)))
        except User.DoesNotExist:
            print(f"\nUser not found.")

        if any(item_id in subscription_plan_ids for item_id in bag_items):
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified ActiveSubscription"s already in database',
                status=200)
        else:
            for plan_id in bag_items:
                subscription_plan = get_object_or_404(SubscriptionPlan, id=plan_id)
                new_subscription = ActiveSubscription(
                    user=user,
                    subscription_plan=subscription_plan,
                    start_date=timezone.now(),
                    end_date=timezone.now() + timezone.timedelta(days=30),
                    status='Active',
                    payment_status='Paid'
                )
                new_subscription.save()
                     
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)



    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)