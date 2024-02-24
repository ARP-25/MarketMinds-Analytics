from django.shortcuts import render
from subscription .models import SubscriptionPlan
from marketminds_analytics import settings

from django.core.mail import send_mail
from django.http import HttpResponse
from django.utils.dateformat import format


# Create your views here.
def index(request):
    """
    A View to return index page
    """
    return render(request, 'home/index.html')



