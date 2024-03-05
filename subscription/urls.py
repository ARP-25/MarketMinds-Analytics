from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required, user_passes_test
from .views import is_superuser



urlpatterns = [
    path('get-started/', views.GetStarted.as_view(), name='get_started'),
    #path('admin-access/', user_passes_test(is_superuser)(views.AdminAccess.as_view()), name='admin_access'),
    path('admin-access/add', user_passes_test(is_superuser)(views.admin_access_add), name='admin_access_add'),
    path('admin-access/edit/<int:subscription_id>/', user_passes_test(is_superuser)(views.admin_access_edit), name='admin_access_edit'),
    path('admin-access/<int:subscription_id>/', user_passes_test(is_superuser)(views.admin_access_delete), name='admin_access_delete'),
]