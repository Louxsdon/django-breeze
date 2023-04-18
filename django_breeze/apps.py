from django.apps import AppConfig
from django_breeze.settings import initialize


class DjangoBreezeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_breeze"

    def ready(self):
        initialize()
