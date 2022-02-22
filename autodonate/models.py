"""Basic objects of donations, items."""

from django.db.models import (
    Model,
    SmallIntegerField,
    FloatField,
    TextField,
    BooleanField,
    ForeignKey,
    CASCADE,
    CharField,
    TimeField,
)
from autodonate.lib.utils.rcon import Rcon
from autodonate.lib.payment.currencies import Currency


class Item(Model):
    """Model for the given item"""

    currency = SmallIntegerField(choices=[(i.value, i.name) for i in Currency], null=True)
    price = FloatField(null=True)
    rcon_command = TextField(null=True)
    require_nick = BooleanField(default=False)


class PaymentProcess(Model):
    """Model for pending item payment"""

    # TODO: Add more fields
    item = ForeignKey(Item, on_delete=CASCADE)
    nickname = CharField(max_length=32, null=True)
    timestamp = TimeField(auto_now_add=True)

    def cleanup_nickname(self) -> None:
        self.nickname = (
            self.nickname.replace(" ", "")
            .replace("'", "")
            .replace('"', "")
            .replace(",", "")
            .replace(".", "")
            .replace("`", "")
        )
        self.save()


class Payment(Model):
    """Model for finished item payment"""

    process = ForeignKey(PaymentProcess, on_delete=CASCADE)
    timestamp = TimeField(auto_now_add=True)

    def format_rcon(self) -> str:
        self.process.cleanup_nickname()
        if not self.process.item.rcon_command:
            raise ValueError("Item.rcon_command required.")
        return str(self.process.item.rcon_command.format(nickname=self.process.nickname))

    def issue(self) -> str:
        return Rcon.run(self.format_rcon())
