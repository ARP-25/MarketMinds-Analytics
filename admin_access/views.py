from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

from subscription.forms import SubscriptionPlanForm
from subscription.models import SubscriptionPlan
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
    A view class for administrative access to manage subscription plans.

    This view handles both GET and POST requests. It displays a list of SubscriptionPlan 
    objects, which can be sorted based on various criteria specified by the 'sort' GET 
    parameter. It also allows administrators to stage and unstage subscription plans through 
    POST requests.

    Attributes:
        - model: SubscriptionPlan model, used to retrieve subscription plan data.
        - template_name: The name of the HTML template used to render the view.
        - context_object_name: The name of the context object to use in the template.

    Supported sorting options:
        - 'most_recent': Sorts the subscription plans by creation date in descending order.
        - 'oldest': Sorts the subscription plans by creation date in ascending order.
        - 'a_z': Sorts the subscription plans alphabetically by title in ascending order.
        - 'z_a': Sorts the subscription plans alphabetically by title in descending order.
        - 'price_desc': Sorts the subscription plans by price in descending order.
        - 'staged': Filters to show only staged subscription plans.
        - 'unstaged': Filters to show only unstaged subscription plans.
        - 'all': Shows all subscription plans without any specific sorting or filtering.

    POST Request Handling:
        - Changes the 'staged' status of a subscription plan identified by 'subscription_id'.
        - Provides success messages and redirects to the 'AdminAccessSubscription' view after
          staging or unstaging operations.

    Methods:
        - post: Handles POST requests to change the staging status of subscription plans.
        - get_queryset: Overrides the default queryset to provide customized sorting and 
          filtering based on the 'sort' parameter in the request.
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
    View function for adding a new subscription plan.

    Handles form submission for adding a new subscription plan.

    Args:
    - request: HTTP request object.

    Returns:
    - Renders the 'admin_access_add.html' template with the form for adding a plan.
    """
    if request.method == 'POST':
        form = SubscriptionPlanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            messages.success(request, 'Subscription Plan has been added successfully!')
            return redirect('AdminAccessSubscription')  
    else:
        form = SubscriptionPlanForm()   
    return render(request, 'admin_access_add.html', {'form': form})

def admin_access_subscription_edit(request, subscription_id):
    """
    View function handling the editing of a subscription plan by ID.

    Retrieves the subscription plan by its ID and renders a form to edit it.
    If the request method is POST and the form is valid, it updates the plan
    and redirects to the 'admin_access' page with a success message.

    Args:
    - request: HTTP request object.
    - subscription_id: ID of the subscription plan to edit.

    Returns:
    - Renders a form to edit the subscription plan details.
    - If the form is submitted and valid, redirects to 'admin_access'
      with a success message after updating the subscription plan.
    """
    subscription = SubscriptionPlan.objects.get(pk=subscription_id) 
    if request.method == 'POST':
        form = SubscriptionPlanForm(request.POST, request.FILES, instance=subscription)
        if form.is_valid():
            form.save()
            messages.success(request, f"{subscription.title} has been edited successfully!")
            return redirect('AdminAccessSubscription') 
    else:
        form = SubscriptionPlanForm(instance=subscription)
    
    return render(request, 'admin_access_edit.html', {'form': form, 'subscription_id': subscription_id})

def admin_access_subscription_delete(request, subscription_id):
    """
    View function for deleting a subscription plan.

    Retrieves and deletes a subscription plan by ID.

    Args:
    - request: HTTP request object.
    - subscription_id: ID of the subscription plan to delete.

    Returns:
    - Redirects to 'admin_access' after successful deletion.
    """
    subscriptionPlan = get_object_or_404(SubscriptionPlan, pk=subscription_id)
    if request.method == 'POST':
        subscriptionPlan.delete()  
        messages.success(request, 'Subscription Plan has been deleted successfully.')
        return redirect('AdminAccessSubscription')  
    return redirect('AdminAccessSubscription')  


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