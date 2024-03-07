from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

from .forms import SubscriptionPlanForm, SubscriptionPlanForm2
from .models import SubscriptionPlan


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

