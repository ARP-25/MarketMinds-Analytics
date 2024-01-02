from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from .models import SubscriptionPlan
from django.contrib import messages


class GetStarted(ListView):
    model = SubscriptionPlan
    template_name = 'get_started.html'
    context_object_name = 'subscription_plans'


