from django.contrib import admin
from django.urls import path
from . import views
from .webhooks import stripe_webhook_handler

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('wh/', stripe_webhook_handler, name='stripe_webhook'),
    path('success/', views.checkout_success, name='checkout_success'),
    path('adjust/<int:item_id>/', views.checkout_adjust, name='checkout_adjust'),
]
