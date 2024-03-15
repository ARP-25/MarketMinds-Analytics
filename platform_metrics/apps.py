from django.apps import AppConfig


class PlatformMetricsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'platform_metrics'

    def ready(self):
        import platform_metrics.signals


  
