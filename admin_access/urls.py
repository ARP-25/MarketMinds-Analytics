from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required, user_passes_test
from .views import is_superuser



urlpatterns = [
    path('',user_passes_test(is_superuser)(views.AdminAccessSubscription.as_view()), name='AdminAccessSubscription'),
    path('add/', user_passes_test(is_superuser)(views.admin_access_subscription_add), name='admin_access_subscription_add'),
    path('edit/<int:subscription_id>/', user_passes_test(is_superuser)(views.admin_access_subscription_edit), name='admin_access_subscription_edit'),
    path('<int:subscription_id>/', user_passes_test(is_superuser)(views.admin_access_subscription_delete), name='admin_access_subscription_delete'),
]