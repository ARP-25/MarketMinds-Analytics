from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_profile, name='view_profile'),
    path('edit/', views.edit_profile, name='edit_profile'), 
    path('cancel-subscription/<int:subscription_id>/', views.cancel_subscription, name='cancel_subscription'),

]
