from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required, user_passes_test


urlpatterns = [
    path('get-started/', views.GetStarted.as_view(), name='get_started'),
]