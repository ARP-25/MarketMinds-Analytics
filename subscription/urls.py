from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('meine-seite/', views.my_view, name='meine_seite'),
    path('subscription-plan/', views.subscription_plan, name='subscription_plan'),
]