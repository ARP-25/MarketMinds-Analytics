from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm  
from bag.contexts import bag_contents
import stripe


# Create your views here.
def checkout(request):

    # Testing if we can access bag from Session and message.error when someone tried to access checkout via URL with an empty shopping bag
    bag = request.session.get('bag_items',[])
    if not bag:
        messages.error(request, 'Theres nopthing in you bnag at the moment')       
    bag_items = request.session.get('bag_items', [])
    print(f"Bag Item ID's:  {request.session.get('bag_items', [])}") 

    # Stripe
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    current_bag = bag_contents(request)
    total = current_bag['total']
    stripe_total = round(total*100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    print(f"\nPayment Intent:{intent}")
    if not stripe_public_key:
        message.warning(request, 'Stripe public key is missing.' 
            'Did you forget to set it in your environment?')


    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)