from django.shortcuts import render
from django.views.generic import ListView
from subscription .models import SubscriptionPlan

# Create your views here.
def index(request):
    """
    A View to return index page
    """
    plans = SubscriptionPlan.objects.all()
    context = {
        'plans' : plans
    }
    return render(request, 'home/index.html', context)