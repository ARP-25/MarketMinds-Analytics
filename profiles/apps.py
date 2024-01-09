from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    Configuration class for the 'profiles' app.

    Attributes:
    - default_auto_field: Sets the default primary key type for models.
    - name: Specifies the app's name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'