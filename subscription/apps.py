from django.apps import AppConfig
from django.apps import apps

class SubscriptionConfig(AppConfig):
    """
    Configuration class for the 'subscription' app.

    Attributes:
    - default_auto_field: Sets the default primary key type for models.
    - name: Specifies the app's name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'subscription'
