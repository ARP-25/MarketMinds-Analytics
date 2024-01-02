from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('bag/', views.bag, name='bag'),
    path('add/', views.add_to_bag, name='add_to_bag'),
]
