from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.trade_insights, name='trade_insights'),
]
