from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import SubscriptionPlan



class GetStartedListView(ListView):
    model = SubscriptionPlan
    template_name = 'subscription/get_started.html'
    context_object_name = 'subscription_plans'

