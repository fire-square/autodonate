"""Models for our project."""
from json import dumps, loads
from secrets import token_urlsafe
from typing import Any, Union

from django.db import models


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
        """Generate random token.

        Returns:
            str: token.
        """
        return token_urlsafe(8)


class Config(models.Model):
    """Configuration model for the application."""

    #: The key of the row.
    key: str = models.CharField(max_length=255, unique=True, primary_key=True)
    #: The value of the row.
    value: str = models.TextField()
    #: Make row available via API.
    public: bool = models.BooleanField(default=False)
    #: Make row immutable for the end user.
    read_only: bool = models.BooleanField(default=False)

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
        return loads(cls.objects.get(key=key).value)

    @classmethod
    def set(cls, key: str, value: Any, public: Union[bool, None] = False, read_only: Union[bool, None] = False) -> None:  # type: ignore[misc]
        """Set (or create) config row in DB.

        Args:
            key: The key of the row.
            value: The value of the row. Can be any type which can understand ``ubjson``.
            public: Make row available via API.
            read_only: Make row immutable for the end user.
        """
        try:
            obj = cls.objects.get(key=key)
        except cls.DoesNotExist:
            obj = cls.objects.create(key=key)
        obj.value = dumps(value)

        if public is not None:
            obj.public = public
        if read_only is not None:
            obj.read_only = read_only

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
        """Pretty output in admin panel."""
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
    #: Item's group.
    group: str = models.CharField(max_length=32, null=True)
    #: Item's image.
    image = models.ImageField(null=True, upload_to="product/covers")
    #: Maximum number of items to buy in one time.
    max_in_cart: int = models.IntegerField(default=1)

    #: Is enabled?
    enabled: bool = models.BooleanField(default=True)

    def __str__(self) -> str:
        """Pretty output in admin panel."""
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
        """Pretty output in admin panel."""
        return str(self.product.name + " - " + self.player.nickname + " - " + str(self.date))
