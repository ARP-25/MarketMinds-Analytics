from django.http import HttpResponse


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
        print("Payment Intent Succeeded")
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f"MarketMinds Webhook received: {event['type']}",
            status=200
        )

    def handle_payment_intent_failed(self, event):
        return HttpResponse(
            content=f"MarketMinds Payment failed Webhook received: {event['type']}",
            status=200
        )

