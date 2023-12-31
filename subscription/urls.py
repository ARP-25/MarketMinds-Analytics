from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('get-started/', views.GetStarted.as_view(), name='get_started'),
    path('admin-access/', views.AdminAccess.as_view(), name='admin_access'),
    path('admin-access/add', views.admin_access_add, name='admin_access_add'),
    path('admin-access/edit/<int:subscription_id>/', views.admin_access_edit, name='admin_access_edit'),
    path('admin-access/<int:subscription_id>/', views.admin_access_delete, name='admin_access_delete'),
]