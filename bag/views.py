from django.shortcuts import render, redirect

# Create your views here.
def bag(request):
    """
    A View to return index page
    """
    return render(request, 'bag/bag.html')

def add_to_bag(request):
    # Fetching subscription_plan_id from the Request Obj
    subscription_plan_id = request.POST.get('subscription_plan_id')

    # Fetching redirect_url from the Request Obj
    redirect_url = request.POST.get('redirect_url')

    # Fetching bag Dictionary or create it and store it locally in variable bag
    bag = request.session.get('bag', [])

    # Add Subscription Plan ID to the bag
    if subscription_plan_id in bag:
        print("You already successfully added this Subscription Plan to your Bag")
    else:
        bag.append(subscription_plan_id)
        request.session['bag'] = bag  # Aktualisiere die 'bag'-Liste in der Session

    # Test if Subscription Plan Id got added to the session bag
    print(request.session.get('bag', []))  # Hier wird die aktualisierte 'bag'-Liste in der Session ausgegeben

    return redirect(redirect_url)