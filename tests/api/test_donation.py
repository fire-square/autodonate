"""Tests for ``/api/donation/`` path."""
from json import loads

from pytest import fixture, mark
from rest_framework.response import Response
from rest_framework.test import APIClient
from structlog import get_logger

from autodonate.models import Config, Donation, Player, Product

log = get_logger()

response: Response = None


def set_up() -> None:
    """Set up some variables for donation testing.

    This called once only in ``conftest.py``, do not touch.

    Raises:
        NameError: When ``test_donation.response`` variable already set,
            so this function called second time.
    """
    products, players = [], []
    for num in range(1, 7):
        product = Product(name=str(num), price=num)
        player = Player(nickname="Steve" + str(num))

        product.save()
        player.save()

        products.append(product)
        players.append(player)

        Donation(product=product, player=player).save()

    global response
    if response is not None:
        raise NameError("This function must be called once!")
    response = APIClient().get("/api/donation/")

    for product in products:
        product.delete()
    for player in players:
        player.delete()


class TestDonation:
    """Tests for ``/api/donation/`` path."""

    @fixture(scope="session")
    def data(self):
        """Parse and return dict with answer."""
        return loads(response.content)

    def test_status_code(self) -> None:
        """``status_code`` must be 200 - okay."""
        assert 200 == response.status_code

    def test_response_len_6(self, data) -> None:
        """API must return only first 6 records."""
        assert len(data) == 6

    def test_correct_order(self, data) -> None:
        """Suring about correct order in response."""
        for i, record in enumerate(data):
            i += 1  # start with 1, not 0
            assert record["product"]["name"] == str(i)
            assert record["product"]["price"] == i
            assert record["player"]["nickname"] == "Steve" + str(i)

    @mark.skip("This is a bug")
    @mark.django_db
    def test_do_not_show_not_enabled_products(self) -> None:
        """If ``product`` is not enabled, it should be hidden."""
        Donation.objects.all().delete()

        products, players = [], []
        for num in range(3):
            product = Product(name=str(num), price=num)
            player = Player(nickname="Steve" + str(num))

            product.save()
            player.save()

            products.append(product)
            players.append(player)

            Donation(product=product, player=player).save()

        response = APIClient().get("/api/donation/")
        assert loads(response.content) == []

        for product in products:
            product.delete()
        for player in players:
            player.delete()
