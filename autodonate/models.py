"""Models for our project."""
from typing import Any

from django.db import models
from ubjson import dumpb, loadb


class Config(models.Model):
    """Configuration model for the application."""

    #: The key of the row.
    key: str = models.CharField(max_length=255, unique=True, primary_key=True)
    #: The value of the row.
    value: str = models.BinaryField(null=True)

    @classmethod
    def get(cls, key: str) -> Any:  # type: ignore[misc]
        """Get row from DB.

        Args:
            key: The key of the row.

        Returns:
            Decoded ``ubjson`` string.

        Raises:
            Config.DoesNotExist: Raised when row does not exist.
        """
        return loadb(cls.objects.get(key=key).value)

    @classmethod
    def set(cls, key: str, value: Any) -> None:  # type: ignore[misc]
        """Set (or create) config row in DB.

        Args:
            key: The key of the row.
            value: The value of the row. Can be any type which can understand ``ubjson``.
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
            ``Config.key``.
        """
        return self.key
