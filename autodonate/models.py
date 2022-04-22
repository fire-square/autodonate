"""Models for our project."""
from django.db import models
from structlog.stdlib import get_logger

log = get_logger()


class Config(models.Model):
    """Configuration for the application."""

    key: str = models.CharField(max_length=255, unique=True, primary_key=True)
    value: str = models.CharField(max_length=255, null=True)
    log.debug("models.Config", key=key, value=value)
