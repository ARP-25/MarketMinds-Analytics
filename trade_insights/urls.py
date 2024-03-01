from django.urls import path
from .views import trade_insights

urlpatterns = [
    path('', trade_insights, name='trade_insights'),

]
