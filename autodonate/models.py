"""Models for our project."""
from typing import Any

from django.db import models
from ubjson import dumpb, loadb


class ConfigKeyDoesNotExist(Exception):
    """Exception for Config.

    Raises when row not found in DB.
    """

    pass


class Config(models.Model):
    """Configuration model for the application."""

    key: str = models.CharField(max_length=255, unique=True, primary_key=True)
    value: str = models.BinaryField(null=True)

    @classmethod
    def get(cls, key: str) -> Any:  # type: ignore
        """Get config row from DB.

        Args:
            key: row name

        Returns:
            Decoded ubjson string.

        Raises:
            ConfigKeyDoesNotExist: when row not found.
        """
        try:
            return loadb(cls.objects.get(key=key).value)
        except cls.DoesNotExist:
            raise ConfigKeyDoesNotExist

    @classmethod
    def set(cls, key: str, value: Any) -> None:  # type: ignore
        """Set (or create) config row in DB.

        Args:
            key: row name
            value: All that understands ubjson (lists, dicts, bool, str, int, bytes...)
        """
        try:
            obj = cls.objects.get(key=key)
        except cls.DoesNotExist:
            obj = cls.objects.create(key=key)
        obj.value = dumpb(value)
        obj.save()

    def __str__(self) -> str:
        """Nice representation in admin panel.

        Returns:
            Config.key.
        """
        return self.key
