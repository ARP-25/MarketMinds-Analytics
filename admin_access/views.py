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
        if 'action' in request.POST:
            action = request.POST['action']
            if action == 'sort_plan':
                return HttpResponse("Sort Plans ausgeführt!")
            elif action == 'delete_plan':
                return HttpResponse("Delete Plan ausgeführt!")
