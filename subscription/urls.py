from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('subscription-plan-list/', views.subscription_plan_list, name='subscription_plan_list'),
]