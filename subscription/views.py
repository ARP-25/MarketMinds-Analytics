from django.shortcuts import render
from .models import SubscriptionPlan
from django.http import HttpResponse

def my_view(request):
    context = {
        'message': 'Hallo von der Django-View!'
    }
    return render(request, 'subscription/mein_template.html', context)

def subscription_plan(request):
    plans = SubscriptionPlan.objects.all()
    context = {
        'plans' : plans
    }
    return render(request, 'subscription/subscription_plan.html', context)