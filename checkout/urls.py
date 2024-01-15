from django.contrib import admin
from django.urls import path
from . import views
from .webhooks import my_webhook_view

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('wh/', my_webhook_view, name='webhook'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
]
