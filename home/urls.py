from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('send-test-email/', views.send_test_email, name='send_test_email'),
]
