from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

from subscription.forms import SubscriptionPlanForm, SubscriptionPlanForm2
from subscription.models import SubscriptionPlan


def is_superuser(user):
    return user.is_superuser


class AdminAccessSubscription(ListView):
    """
    View class for administrative access.

    Handles POST requests for sorting or deleting subscription plans.

    Attributes:
    - model: SubscriptionPlan model for retrieving data.
    - template_name: HTML template to render.
    - context_object_name: Name of the context object in the template.
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
        elif sort == 'price_asc':
            queryset = queryset.order_by('price')

        return queryset


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
        return redirect('admin_access')  
    return redirect('admin_access')  


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
            return redirect('admin_access')  
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
        form = SubscriptionPlanForm2(request.POST, request.FILES, instance=subscription)
        if form.is_valid():
            form.save()
            messages.success(request, f"{subscription.title} has been successfully edited!")
            return redirect('admin_access') 
    else:
        form = SubscriptionPlanForm(instance=subscription)
    
    return render(request, 'admin_access_edit.html', {'form': form, 'subscription_id': subscription_id})
