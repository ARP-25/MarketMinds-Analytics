from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

from .forms import SubscriptionPlanForm, SubscriptionPlanForm2
from .models import SubscriptionPlan


def is_superuser(user):
    return user.is_superuser

class GetStarted(ListView):
    """
    View class for displaying subscription plans.

    Retrieves and displays subscription plans using ListView.

    Attributes:
    - model: SubscriptionPlan model for retrieving data.
    - template_name: HTML template to render.
    - context_object_name: Name of the context object in the template.
    - paginate_by: Number of items to paginate per page.
    """
    model = SubscriptionPlan
    template_name = 'get_started.html'
    context_object_name = 'subscription_plans'
    paginate_by = 6  

    def get_queryset(self):
        return SubscriptionPlan.objects.order_by('id')


class AdminAccess(ListView):
    """
    View class for administrative access.

    Handles POST requests for sorting or deleting subscription plans.

    Attributes:
    - model: SubscriptionPlan model for retrieving data.
    - template_name: HTML template to render.
    - context_object_name: Name of the context object in the template.
    """
    model = SubscriptionPlan
    template_name = 'admin_access.html'
    context_object_name = 'subscription_plans'


    def post(self, request, *args, **kwargs):
        if 'action' in request.POST:
            action = request.POST['action']
            if action == 'sort_plan':
                return HttpResponse("Sort Plans ausgeführt!")
            elif action == 'delete_plan':
                return HttpResponse("Delete Plan ausgeführt!")


def admin_access_add(request):
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
            return redirect('admin_access')  
    else:
        form = SubscriptionPlanForm()   
    return render(request, 'admin_access_add.html', {'form': form})


def admin_access_delete(request, subscription_id):
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
        return redirect('admin_access')  
    return redirect('admin_access')  



def admin_access_edit(request, subscription_id):
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
        form = SubscriptionPlanForm2(request.POST, request.FILES, instance=subscription)
        if form.is_valid():
            form.save()
            messages.success(request, f"{subscription.title} has been successfully edited!")
            return redirect('admin_access') 
    else:
        form = SubscriptionPlanForm(instance=subscription)
    
    return render(request, 'admin_access_edit.html', {'form': form, 'subscription_id': subscription_id})

