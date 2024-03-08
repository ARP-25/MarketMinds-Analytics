from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required, user_passes_test
from .views import is_superuser



urlpatterns = [
    path('subscription/',user_passes_test(is_superuser)(views.AdminAccessSubscription.as_view()), name='AdminAccessSubscription'),
    path('subscription/add/', user_passes_test(is_superuser)(views.admin_access_subscription_add), name='admin_access_subscription_add'),
    path('subscription/edit/<int:subscription_id>/', user_passes_test(is_superuser)(views.admin_access_subscription_edit), name='admin_access_subscription_edit'),
    path('subscription/<int:subscription_id>/', user_passes_test(is_superuser)(views.admin_access_subscription_delete), name='admin_access_subscription_delete'),
    path('insight/',user_passes_test(is_superuser)(views.AdminAccessInsight.as_view()), name='AdminAccessInsight'),
    path('insight/add/', user_passes_test(is_superuser)(views.admin_access_insight_add), name='admin_access_insight_add'),
    path('insight/edit/<int:insight_id>/', user_passes_test(is_superuser)(views.admin_access_insight_edit), name='admin_access_insight_edit'),
]