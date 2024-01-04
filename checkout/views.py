from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm  

# Create your views here.
def checkout(request):
    bag = request.session.get('bag_items',[])
    if not bag:
        messages.error(request, 'Theres nopthing in you bnag at the moment')
        
    bag_items = request.session.get('bag_items', [])
    print(request.session.get('bag_items', []))  

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OOhcmL1KLkVpLL6W36Gld3ByPSZJP1lwqC0nxwXtjp7JcIwgfXU3QnsOewy7i3RXddHzXMT6CpIjdJyIU6ae2Of000YX9CcCP',
        'client_secret': 'test_client_secret'
    }

    return render(request, template, context)