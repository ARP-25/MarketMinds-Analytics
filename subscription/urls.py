from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('get-started/', views.GetStarted.as_view(), name='get_started'),
    path('admin-access/', views.AdminAccess.as_view(), name='admin_access'),
]