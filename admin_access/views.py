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
    return user.is_superuser

# Admin Acces Subscription
class AdminAccessSubscription(ListView):
    """
    A view class for administrative access to manage subscription plans.

    This class handles both GET and POST requests. It supports sorting subscription plans 
    based on various criteria such as creation date, title, price, and staging status. 
    It also allows for staging and unstaging subscription plans through POST requests.

    Attributes:
    - model: SubscriptionPlan model, used to retrieve subscription plan data.
    - template_name: String, the name of the HTML template used to render the view.
    - context_object_name: String, the name of the context object to use in the template.

    The view supports sorting by:
    - Most recent creation ('most_recent')
    - Oldest creation ('oldest')
    - Alphabetically by title ('a_z', 'z_a')
    - Price ('price_desc')
    - Staged status ('staged', 'unstaged')
    - All subscription plans without filter ('all')

    POST requests are used to change the 'staged' status of subscription plans, with
    appropriate success messages and redirection to the 'AdminAccessSubscription' view.
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
            messages.success(request, 'Successfully added new Subscription Plan!')
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
            messages.success(request, f"{subscription.title} has been successfully edited!")
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
        messages.success(request, 'Subscription Plan deleted successfully.')
        return redirect('AdminAccessSubscription')  
    return redirect('AdminAccessSubscription')  


# Admin Access Trade Insight
class AdminAccessInsight(ListView):

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
        # Your filtering/sorting logic goes here
        return queryset

def admin_access_insight_add(request):
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


#def admin_accesss_insight_delete(request, insight_id):