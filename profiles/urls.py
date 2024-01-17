from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required, user_passes_test

urlpatterns = [
    path('', login_required(views.view_profile), name='view_profile'),
    path('edit/', login_required(views.edit_profile), name='edit_profile'), 
    path('cancel-subscription/<int:subscription_id>/', login_required(views.cancel_subscription), name='cancel_subscription'),
]
