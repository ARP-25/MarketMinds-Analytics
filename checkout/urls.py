from django.contrib import admin
from django.urls import path
from . import views
from .webhooks import my_webhook_view

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('2', views.checkout2, name='checkout2'),
    path('wh/', my_webhook_view, name='webhook'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('success/', views.checkout_success, name='checkout_success'),
    path('adjust/<int:item_id>/', views.checkout_adjust, name='checkout_adjust'),
]
