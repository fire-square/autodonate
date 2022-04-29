"""Models for our project."""
from secrets import token_urlsafe
from typing import Any

from django.db import models
from ubjson import dumpb, loadb


class TokenField(models.CharField):
    """Custom Field for automatic ID assign."""

    def __init__(self, *args, **kwargs) -> None:
        """__init__ method."""
        kwargs["max_length"] = 12
        kwargs["primary_key"] = True
        kwargs["default"] = self.generate
        super().__init__(*args, **kwargs)

    @staticmethod
    def generate() -> str:
        return token_urlsafe(8)


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


class Player(models.Model):
    """Player model. Represents minecraft player."""

    #: Nickname of the player.
    nickname = models.CharField(max_length=32, primary_key=True)

    def __str__(self) -> str:
        """Str representation."""
        return str(self.nickname)


class Product(models.Model):
    """Product model. Represents an item to buy."""

    #: Unique string identifier.
    id = TokenField()
    #: Item's name.
    name: str = models.CharField(max_length=255, unique=True)
    #: Item's price.
    price: int = models.IntegerField()
    #: Item's long description.
    long_description: str = models.TextField(null=True)
    #: Item's image.
    image = models.ImageField(null=True, upload_to="product/covers")
    #: Maximum number of items to buy in one time.
    max_in_cart: int = models.IntegerField(default=1)

    def __str__(self) -> str:
        """Str representation."""
        return self.name


class Donation(models.Model):
    """Represents a record when player buy donation."""

    #: Unique string identifier.
    id = TokenField()
    #: Product which was bought.
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    #: Donation's player, which bought donation.
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    #: Date when the donation was made.
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """Str representation."""
        return str(self.product.name + " - " + self.player.nickname + " - " + str(self.date))
