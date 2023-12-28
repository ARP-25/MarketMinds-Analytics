from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('subscription-plan/', views.subscription_plan, name='subscription_plan'),
]