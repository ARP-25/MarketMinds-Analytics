from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

    def ready(self):
        # Beispielcode, der auf django_summernote zugreift
        try:
            # Zugriff auf die Konfiguration von django_summernote
            summernote_config = apps.get_app_config('django_summernote').config
            # Hier könntest du weitere Aktionen mit der Summernote-Konfiguration durchführen
        except Exception as e:
            # Behandlung von Fehlern, falls erforderlich
            pass
