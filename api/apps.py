"""App module for API app."""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """API configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "api"
