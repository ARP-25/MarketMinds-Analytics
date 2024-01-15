from django.http import HttpResponse
import stripe

class StripeWH_Handler:

    def __init__(self, request):
        self.request = request
    
    def handle_event(self, event):
        print(f"Handling event: {event['type']}")
        return HttpResponse(
            content=f"MarketMinds Unhandled webhook received: {event['type']}",
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details # updated
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2) # updated
        return HttpResponse(
            content=f"MarketMinds Webhook received: {event['type']}",
            status=200
        )

    def handle_payment_intent_failed(self, event):
        return HttpResponse(
            content=f"MarketMinds Payment failed Webhook received: {event['type']}",
            status=200
        )

