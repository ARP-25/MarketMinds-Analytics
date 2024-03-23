from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings

import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

from platform_metrics.models import FinancialMetrics
from subscription.forms import SubscriptionPlanForm
from subscription.models import SubscriptionPlan
from checkout.models import ActiveSubscription
from trade_insights.models import Insight
from .forms import InsightForm



def is_superuser(user):
    """
    Determines if the given user is a superuser.

    This function checks the 'is_superuser' attribute of the user object 
    to determine if the user has superuser privileges.

    Args:
        user (User): The user object to be checked for superuser status.

    Returns:
        bool: True if the user is a superuser, False otherwise.
    """
    return user.is_superuser

# Admin Acces Subscription
class AdminAccessSubscription(ListView):
    """
    A ListView for managing subscription plans in the administrative interface.

    This view displays a list of SubscriptionPlan objects and supports various sorting 
    and filtering options. It also allows administrators to toggle the 'staged' status 
    of subscription plans via POST requests, facilitating the management of which 
    plans are available or featured.

    Attributes:
        - model: The SubscriptionPlan model, specifying the source of the data.
        - template_name: The template used to render the subscription plans list.
        - context_object_name: The name of the context object in the template.

    Supported Sorting and Filtering Options:
        The view supports sorting by most recent, oldest, alphabetical order (A-Z, Z-A), 
        price, and filtering by staged or unstaged status. The default view shows all 
        plans without specific sorting or filtering.

    POST Request Handling:
        Processes POST requests to stage or unstage subscription plans based on the 
        'subscription_id' provided in the request. It updates the 'staged' attribute 
        of the corresponding SubscriptionPlan and displays a success message.

    Methods:
        - post: Handles POST requests to change the 'staged' status of subscription plans.
        - get_queryset: Overrides the default queryset to apply the sorting and filtering 
          logic based on the 'sort' parameter received in the GET request.

    Note:
        This view is intended for use by administrators or staff members with appropriate 
        permissions to manage subscription plans.
    """
    model = SubscriptionPlan
    template_name = 'admin_access/admin_access_subscription.html'
    context_object_name = 'subscription_plans'

 
    def post(self, request, *args, **kwargs):
        if 'action' in request.POST and request.POST['action'] == 'stage':
            subscription_id = request.POST.get('subscription_id')
            subscription_plan = get_object_or_404(SubscriptionPlan, pk=subscription_id)
            subscription_plan.staged = True
            subscription_plan.save()
            messages.success(request, 'Subscription Plan has been staged successfully.')
            return redirect('AdminAccessSubscription')
        else:
            subscription_id = request.POST.get('subscription_id')
            subscription_plan = get_object_or_404(SubscriptionPlan, pk=subscription_id)
            subscription_plan.staged = False
            subscription_plan.save()
            messages.success(request, 'Subscription Plan has been unstaged successfully.')
            return redirect('AdminAccessSubscription')
        return redirect('AdminAccessSubscription')

    def get_queryset(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort')

        if sort == 'most_recent':
            queryset = queryset.order_by('-created_at') 
        elif sort == 'oldest':
            queryset = queryset.order_by('created_at')
        elif sort == 'a_z':
            queryset = queryset.order_by('title')
        elif sort == 'z_a':
            queryset = queryset.order_by('-title')
        elif sort == 'price_desc':
            queryset = queryset.order_by('-price')
        elif sort == 'staged':
            queryset = queryset.filter(staged=True)
        elif sort == 'unstaged':
            queryset = queryset.filter(staged=False)
        elif sort == 'all':
            queryset = super().get_queryset()            

        return queryset


def admin_access_subscription_add(request):
    """
    View function for creating and adding a new subscription plan to the Stripe platform 
    and the Django application database.

    This view handles two primary tasks:
    1. On a GET request, it renders a form to add a new subscription plan.
    2. On a POST request, it processes the submitted form to create a subscription plan.
       If the form is valid, the function creates a corresponding product and price in Stripe 
       and saves the new subscription plan in the Django database, including the Stripe 
       price ID. If the form is invalid, it re-renders the form with error messages.

    The Stripe product creation includes an image URL from an S3 bucket, if provided. The 
    Stripe price creation includes metadata from the form, such as title, description, 
    details, price, and an indication that this was an 'add action'. In the Django database, 
    the subscription plan is saved with the Stripe price ID.

    Args:
    - request (HttpRequest): The Django request object.

    Returns:
    - HttpResponse: Renders the subscription plan addition form on a GET request. On a POST request,
      processes the form, and based on its validity, either creates a new subscription plan and 
      redirects to the 'AdminAccessSubscription' page, or re-renders the form with error messages.

    Notes:
    - This view function requires a valid Stripe API setup and a corresponding SubscriptionPlanForm.
    - The view communicates with Stripe's API to create new products and prices and handles Stripe 
      errors appropriately.
    - Success and error messages are used to provide feedback to the user.
    """
    if request.method == 'POST':
        form = SubscriptionPlanForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                details = form.cleaned_data.get('details', '')
                price = int(form.cleaned_data['price'] * 100)
                image_url = form.cleaned_data.get('image', '')
                
                stripe_product = stripe.Product.create(
                    name=title,
                    images=image_url
                )
                # Creating the price in Stripe with local image URL/Filename
                stripe_price = stripe.Price.create(
                    unit_amount=price,
                    currency='usd',
                    recurring={"interval": "month"},
                    product=stripe_product.id,
                    metadata={ 
                        'title': title,
                        'description': description,
                        'details': details,
                        'price': form.cleaned_data['price'],
                        'image_url': image_url,
                        'add_action': 'true'  
                    }
                )
                subscription_plan = form.save(commit=False)
                subscription_plan.stripe_price_id = stripe_price.id
                subscription_plan.save()

                messages.success(request, 'Subscription Plan has been added successfully!')
                return redirect('AdminAccessSubscription')
            except stripe.error.StripeError as e:
                messages.error(request, f"Stripe error: {e}")
        else:
            messages.error(request, "There was a problem with the form. Please check the details.")
    else:
        form = SubscriptionPlanForm()

    return render(request, 'admin_access_add.html', {'form': form})


def admin_access_subscription_edit(request, subscription_id):
    subscription = get_object_or_404(SubscriptionPlan, pk=subscription_id) 
    original_price = subscription.price  

    if request.method == 'POST':
        form = SubscriptionPlanForm(request.POST, request.FILES, instance=subscription)
        if form.is_valid():
            is_price_changed = form.cleaned_data['price'] != original_price
            metadata = {'django_plan_id': subscription.id, 'created_by_admin': True}
            print(f"is_price_changed:", is_price_changed)
            if is_price_changed:
                try:
                    title = form.cleaned_data['title']
                    description = form.cleaned_data['description']
                    details = form.cleaned_data.get('details', '')
                    new_price = int(form.cleaned_data['price'] * 100)
                    image_url = form.cleaned_data.get('image', '')

                    stripe_product = stripe.Product.create(name=title, images=[s3_image_url])

                    metadata = {
                        'title': title,
                        'description': description,
                        'details': details,
                        'price': form.cleaned_data['price'],
                        'image_url': image_url,
                    }
                    # Determine whether to create a new plan or update the existing one
                    active_subscriptions_exist = ActiveSubscription.objects.filter(subscription_plan=subscription).exists()

                    if active_subscriptions_exist:
                        metadata['add_action'] = 'true'
                    else:
                        metadata['edit_action'] = 'true'

                    stripe_price = stripe.Price.create(
                        unit_amount=new_price,
                        currency='usd',
                        recurring={"interval": "month"},
                        product=stripe_product.id,
                        metadata=metadata
                    )
                    print(f"\n\nmetadata: {metadata}\n\n")
                    subscription.stripe_price_id = stripe_price.id
                except stripe.error.StripeError as e:
                    messages.error(request, f"Stripe error: {e}")
                    return render(request, 'admin_access_edit.html', {'form': form, 'subscription_id': subscription_id})

            if not is_price_changed or not active_subscriptions_exist:
                # Update the plan in Django (if price hasn't changed or there are no active subscriptions)
                subscription.save()

            messages.success(request, f"{subscription.title} has been edited successfully!")
            return redirect('AdminAccessSubscription') 
    else:
        form = SubscriptionPlanForm(instance=subscription)
    
    return render(request, 'admin_access_edit.html', {'form': form, 'subscription_id': subscription_id})


def admin_access_subscription_delete(request, subscription_id):
    """
    Handles the deletion of a subscription plan.

    This view function is called when an admin user requests to delete a subscription plan. 
    It checks if the subscription plan is referenced in any active subscriptions. 
    If it is, the plan is not deleted but marked as invisible (staged = False), so it's no longer visible 
    on the front end but still exists for active subscriptions. 
    If no active subscriptions reference the plan, it checks with Stripe to see if the plan can be deleted there. 
    If so, the plan is deleted in both Stripe and the Django database.

    Args:
    - request: The HTTP request object.
    - subscription_id: The ID of the subscription plan to delete.

    Returns:
    - A redirect to the 'AdminAccessSubscription' view.
    """
    try:
        subscriptionPlan = get_object_or_404(SubscriptionPlan, pk=subscription_id)
        if ActiveSubscription.objects.filter(subscription_plan=subscriptionPlan).exists():
            subscriptionPlan.staged = False
            subscriptionPlan.save()
            messages.info(request, f"The plan '{subscriptionPlan.title}' is still in active subscriptions and has been marked as invisible.")
        else:
            stripe_subscriptions = stripe.Subscription.list(plan=subscriptionPlan.stripe_price_id)
            if not stripe_subscriptions['data']:
                stripe.Plan.delete(subscriptionPlan.stripe_price_id)
                subscriptionPlan.delete()
                messages.success(request, f"The plan '{subscriptionPlan.title}' was successfully deleted.")
            else:
                print(f"\nWere in else block\n subscriptionPlan.staged:{subscriptionPlan.staged}\n")
                print(f"\nWere in else block\n subscriptionPlan.id:{subscriptionPlan.id}\n")
                subscriptionPlan.staged = False
                print(f"\nShould have set on False now\n subscriptionPlan:{subscriptionPlan.staged}\n")
                print(f"\nShould have set on False now\n subscriptionPlan.id:{subscriptionPlan.id}\n")
                messages.warning(request, f"The plan '{subscriptionPlan.title}' cannot be deleted as it is still in use in Stripe and would compromsie Database integrity. The Subscription Plan will be marked as insivsible instead.")
    except Exception as e:
        messages.error(request, f"An error occurred: {e}")
    print(f"\nShould still be on False now\n subscriptionPlan:{subscriptionPlan.staged}\n")
    print(f"\nShould still be on False now\n subscriptionPlan.id:{subscriptionPlan.id}\n")
    return redirect('AdminAccessSubscription')


def remove_plan_from_bag(request, subscription_id):
    """
    Removes a given subscription plan ID from the 'bag_items' session variable.
    
    Args:
    - request: The HTTP request object.
    - subscription_id: The ID of the subscription plan to remove.

    Returns:
    - None
    """
    bag_items = request.session.get('bag_items', [])
    if str(subscription_id) in bag_items:
        bag_items.remove(str(subscription_id))
        request.session['bag_items'] = bag_items
        messages.info(request, 'Removed deleted plan from your bag.')


# Admin Access Trade Insight
class AdminAccessInsight(ListView):
    """
    This view provides an interface for administrators to access and manage insights.

    The view displays a list of Insight objects, which can be sorted and filtered based on different criteria specified by the 'sort' GET parameter. The available sorting and filtering options include:

    - 'most_recent': Sorts the insights by release_date in descending order, showing the newest insights first.
    - 'oldest': Sorts the insights by release_date in ascending order.
    - 'a_z': Sorts the insights alphabetically by title in ascending order.
    - 'z_a': Sorts the insights alphabetically by title in descending order.
    - 'crypto', 'forex', 'stocks': Filters and shows only the insights that are associated with the respective 'SubscriptionPlan' category titles.
    - 'mainstage', 'secondstage', 'backstage': Filters and shows only the insights that are in the specified stage (Mainstage, Secondstage, Backstage).
    - 'all': Shows all insights without any specific sorting or filtering.

    The sorted or filtered insights are displayed to the admin user in 'admin_access/admin_access_insight.html'. The view ensures that the insights are presented in a manner that is easy to navigate and manage for administrative purposes.

    Attributes:
        model: Specifies the model to be used in the list view (Insight).
        template_name: Designates the HTML template used to render the list view ('admin_access/admin_access_insight.html').
        context_object_name: Defines the context name in which the list will be passed to the template ('trade_insights').

    Methods:
        get_queryset: Overrides the default queryset to provide customized sorting and filtering based on the 'sort' parameter in the request.
    """  
    model = Insight
    template_name = 'admin_access/admin_access_insight.html'
    context_object_name = 'trade_insights'

    def get_queryset(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort')

        if sort == 'most_recent':
            queryset = queryset.order_by('-release_date') 
        elif sort == 'oldest':
            queryset = queryset.order_by('release_date')
        elif sort == 'crypto':
            queryset = Insight.objects.filter(category__title='Crypto')
        elif sort == 'forex':
            queryset = Insight.objects.filter(category__title='Forex')   
        elif sort == 'stocks':
            queryset = Insight.objects.filter(category__title='Stocks')  
        elif sort == 'a_z':
            queryset = queryset.order_by('title')
        elif sort == 'z_a':
            queryset = queryset.order_by('-title')
        elif sort == 'mainstage':
            queryset = Insight.objects.filter(stage='MS')
        elif sort == 'secondstage':
            queryset = Insight.objects.filter(stage='SS')
        elif sort == 'backstage':
            queryset = Insight.objects.filter(stage='BS')
        elif sort == 'all':
            queryset = super().get_queryset()
          
        return queryset


def admin_access_insight_add(request):
    """
    Handles the addition of a new Insight object through an admin interface.

    This view manages the creation and submission of a new Insight object. If the request method is POST and the submitted form is valid, a new Insight object is created and saved. Upon successful creation, a success message is displayed, and the user is redirected to the 'AdminAccessInsight' view. If the request method is not POST, an empty form is presented to the user for submission.

    Args:
        request: The HttpRequest object containing metadata about the request.

    Returns:
        If the request method is POST and the form is valid, redirects to the 'AdminAccessInsight' view.
        If the request method is not POST, renders the 'admin_access/admin_access_insight_add.html' template with the form.

    Note:
        This function uses the InsightForm for data validation and creation of Insight objects.
    """    
    if request.method == 'POST':
        form = InsightForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            messages.success(request, 'Successfully added new Insight!')
            return redirect('AdminAccessInsight')  
    else:
        form = InsightForm()   
    return render(request, 'admin_access/admin_access_insight_add.html', {'form': form})


def admin_access_insight_edit(request, insight_id):
    """
    View function for editing an existing trade insight.

    This function retrieves an existing trade insight by its ID and presents a form for editing it.
    If the request method is POST and the submitted form is valid, the insight is updated in the database.
    Upon successful update, a success message is displayed and the user is redirected to the list of all insights.

    Args:
    - request: The HTTP request object.
    - insight_id: The ID of the insight to be edited.

    Returns:
    - An HttpResponse object that renders the 'admin_access/admin_access_insight_edit.html' template.
      This template includes the form for editing the insight.
    - If the form is submitted and valid, redirects to the 'AdminAccessInsight' view, indicating
      successful editing with a success message.
    """
    insight = Insight.objects.get(pk=insight_id) 
    if request.method == 'POST':
        form = InsightForm(request.POST, request.FILES, instance=insight)
        if form.is_valid():
            form.save()
            messages.success(request, f"{insight.title} has been successfully edited!")
            return redirect('AdminAccessInsight')

    else:
        form = InsightForm(instance=insight)
    form = InsightForm(instance=insight)
    return render(request, 'admin_access/admin_access_insight_edit.html', {'form': form,'insight_id': insight_id})


def admin_access_insight_delete(request, insight_id):
    """
    Deletes a specified Insight object.

    This view handles the deletion of an Insight object identified by the provided insight_id. It is intended to be used in an admin context where a POST request triggers the deletion. A success message is displayed upon successful deletion.

    Args:
        request: The HttpRequest object containing metadata about the request.
        insight_id: The primary key of the Insight object to be deleted.

    Returns:
        A redirect to the 'AdminAccessInsight' view.

    Note:
        This function only processes POST requests for deletion to ensure safe deletion operations. Any other type of request will result in a redirect without deletion.
    """
    insight = get_object_or_404(Insight, pk=insight_id)
    if request.method == 'POST':
        insight.delete()  
        messages.success(request, 'Trade Insight has been deleted successfully.')
        return redirect('AdminAccessInsight')  
    return redirect('AdminAccessInsight')  


# Admin Access Trade Insight
class AdminAccessMetric(ListView):
    """
    A ListView for displaying financial metrics in the administrative interface.

    This view is specifically designed for administrators to access and review financial 
    metrics captured by the system. It lists instances of the FinancialMetrics model, 
    providing a comprehensive view of financial data like revenue, subscriptions, and 
    other related metrics.

    Attributes:
        - model: Specifies the FinancialMetrics model to define the source of data.
        - template_name: The name of the template used to render the financial metrics.
        - context_object_name: The name of the context object to use in the template. This is 
          used to refer to the list of financial metrics in the template.

    Methods:
        - get_queryset: Overrides the default queryset to provide sorting functionality. The 
          sorting criteria are specified via a 'sort' parameter in the request's GET data.

    Notes:
        - The view can be extended to include filtering and more advanced sorting capabilities 
          based on different attributes of the FinancialMetrics model.
        - The current implementation of `get_queryset` provides basic sorting functionality. 
          Further customization can be added as required for more complex data handling.
    """
    model = FinancialMetrics
    template_name = 'admin_access/admin_access_metric.html'
    context_object_name = 'trade_insights'

    def get_queryset(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort')

        return queryset
