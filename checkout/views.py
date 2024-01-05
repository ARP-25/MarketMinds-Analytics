from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse
from .forms import OrderForm  
from bag.contexts import bag_contents
import stripe



def checkout(request):
    """
    bag_items = request.session.get('bag',[])
    # Handle Logic on checkout form submit, Orderline Item needs to get created from bag_items ID's
    if request.method == 'POST':

        # Check if this message appears
        print("Form is being submitted")  
        
        print(bag_items)

        # Fetching Checkout Form Daten
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        # Intanzierung von OrderForm Objekt mit Formdaten, mit diesem Objekt kann man später
        # ein Order Objekt mit den Formdaten instanzieren.
        order_form = OrderForm(form_data)
        if order_form.is_valid():        
            # Hier füllen wir die Variable order mit Form Daten, später intanziieren wird ein Order Objekt mit diesen Daten
            order = order_form.save()

            # Hier soll order_line_item.save() ausgelöst werden, damit auch eine order in Database gepspeichert wird
            # Iterieren über unser bag_items Array
            for item_id in bag_items:
                print(item_id)
                try:

                    # Hier wird das Subscription Plan Objekt mit item_id als ID gespeichert
                    subscription_plan = SubscriptionPlan.objects.get(id=item_id)
                    print(f"\nSubscription Plan das in for Loop gefetched wird:{subscription_plan}")
                    # Hier wird ein OrderLineItem Objekt instanziiert mit den Formulardaten und dem gerade mit ID bestimmten Objekt
                    order_line_item = OrderLineItem(
                        order=order,
                        subscription_plan=subscription_plan,
                    )
                    print(f"\nOrder Line Item das in for Loop gefetched wird:{order_line_item}")

                    # Hier wird OrderLineItem gesaved und damit usner signal getriggert und somit Order gespeichert im Backend
                    order_line_item.save()

                # Error wird gecatched falls ein Subscription Plan ID aus bag_items in unseren Subscription Plänen nicht gefunden wird.
                except SubscriptionPlan.DoesNotExist:
                    messages.error(request, (
                        "One of the subscription_plans in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('checkout/checkout'))

        #return HttpResponse(render(request, 'checkout/checkout.html'))
        


    """
    # Testing if we can access bag from Session and message.error when someone tried to access checkout via URL with an empty shopping bag
    bag = request.session.get('bag_items',[])
    if not bag:
        messages.error(request, 'Theres nopthing in you bnag at the moment')       
    bag_items = request.session.get('bag_items', [])
    #print(f"Bag Item ID's:  {request.session.get('bag_items', [])}") 

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

    #print(f"\nPayment Intent:{intent}")
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