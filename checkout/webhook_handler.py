from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import ActiveSubscription
from subscription.models import SubscriptionPlan

import json
import time

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)



    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        
        # Hier retrieven wir Daten von webhook event
        intent = event.data.object
        bag_items = intent.metadata.bag
        print(f"\nBag: {bag_items}")
        user_name = intent.metadata.username
        print(f"\nUsername: {user_name}")

        # Benutzer ID mit dem erhaltenen Benutzernamen abrufen und damit nach ActiveSubscriptions suchen
        # und direkt Die associateten Plan ID's identifizieren
        try:
            user = User.objects.get(username=user_name)
            print(f"\nUser ID: {user.id}")
            subscription_plan_ids = ActiveSubscription.objects.filter(user=user.id).values_list('subscription_plan__id', flat=True)
            print(f"\nActive Subscritions with its associated SubscriptionPlan ID's from identified User: {subscription_plan_ids}\n")
        except User.DoesNotExist:
            print("\nBenutzer nicht gefunden.")

        # Checken of wir ActiveSubscriptions auf Benutzer ID haben
        

        # Check if the user already has the ActiveSubscription
        """

        save_info = intent.metadata.save_info
        print(f"\nBilling details:{save_info}")      
        billing_details = intent.charges.data[0].billing_details
        print(f"\nBilling_details: {billing_details}")
        shipping_details = intent.shipping
        print(f"\nshipping_details: {shipping_details}")
        grand_total = round(intent.charges.data[0].amount / 100, 2)
        print(f"\n{grand_total}")
        """
        """
        # Clean data in the shipping details. Alle Felder die nicht ausgefüllt wurden werdenauf None gesetzt anstelle eines leeren Strings.
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Hier entsteht Loogik um abzuprüfen ob die Order bereits durch den Form submit exisitert.
        # Es wird 5x attempted jeweils 1 Sekunde lang. Da wir hier asynchron arbeiten versuchen wir den Servern Zeit zu lassen.
        # Ansonsten könnte es passieren, dass wir fälschlicherweise die ActiveSubscription einmal durch Form Submit speichern
        # und danach noch einmal durch WH Handler
        active_subscription_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                active_subscription = ActiveSubscription.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                active_subscription_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)

        # Falls Active Subscription noch nicht existiert, sollte sie hier initialisiert werden        
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()

            # Error throwen wenn bei Active Subscription Creation etwas fehlschlägt
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        """

        # Wenn ActiveSubscription bereits durch Form submit created wurde oder gerade von WH Handler created wurde landen wir hier und antworten auf den webhook.
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