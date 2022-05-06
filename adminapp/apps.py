"""Admin app."""

from django.apps import AppConfig


class AdminappConfig(AppConfig):
    """Admin app config."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "adminapp"
