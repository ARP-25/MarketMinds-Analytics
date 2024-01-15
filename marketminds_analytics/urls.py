from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404
from .views import handler404, render_custom_404


urlpatterns = [   
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('', include('home.urls')),
    path('', include('subscription.urls')),
    path('', include('bag.urls')),     
    path('checkout/', include('checkout.urls')),     
    path('profile/', include('profiles.urls')),  
    path('trade-insights/', include('trade_insights.urls')),  
    path('render-404/', render_custom_404, name='render_404'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'marketminds_analytics.views.handler404'