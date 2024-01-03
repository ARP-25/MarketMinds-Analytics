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
    }

    return render(request, template, context)