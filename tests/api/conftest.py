"""Shared fixtures for tests in ``api/`` folder."""
from django.core.management import call_command
from pytest import fixture

from autodonate.models import Config
from tests import api


@fixture(scope="session", autouse=True)
def django_db_setup(django_db_setup, django_db_blocker):
    """Additional setup DB steps."""
    with django_db_blocker.unblock():
        api.test_config.set_up()
        api.test_product.set_up()
        api.test_player.set_up()
        api.test_donation.set_up()
