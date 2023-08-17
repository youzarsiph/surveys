""" AppConf """


from django.apps import AppConfig


# Create your conf here.
class UsersConfig(AppConfig):
    """App Configuration for surveys app"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "surveys"
