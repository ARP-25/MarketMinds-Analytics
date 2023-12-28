from django.shortcuts import render
from .models import SubscriptionPlan
from django.http import HttpResponse


def subscription_plan_list(request):
    plans = SubscriptionPlan.objects.all()
    context = {
        'plans' : plans
    }
    return render(request, 'subscription/subscription_plan_list.html', context)
