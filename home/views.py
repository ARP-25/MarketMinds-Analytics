from django.shortcuts import render
from subscription .models import SubscriptionPlan

# Create your views here.
def index(request):
    """
    A View to return index page
    """
    return render(request, 'home/index.html')