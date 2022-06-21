"""Tests for ``/api/config/`` path."""
from json import loads

from pytest import fixture, mark
from rest_framework.response import Response
from rest_framework.test import APIClient
from structlog import get_logger

from autodonate.models import Config

log = get_logger()

response: Response = None


def set_up() -> None:
    """Set up some variables for config testing.

    This called once only in ``conftest.py``, do not touch.

    Raises:
        NameError: When ``test_config.response`` variable already set,
            so this function called second time.
    """
    Config.set("something1", "1", True)
    Config.set("something2", "2", True)
    Config.set("something3", "3", False)

    global response
    if response is not None:
        raise NameError("This function must be called once!")
    response = APIClient().get("/api/config/")


class TestConfig:
    """Tests for ``/api/config/`` path."""

    @fixture(scope="session")
    def data(self):
        """Parse and return dict with answer."""
        return loads(response.content)

    def test_status_code(self) -> None:
        """``status_code`` must be 200 - okay."""
        assert 200 == response.status_code

    @mark.parametrize(
        "key,value",
        [
            ("something1", '"1"'),
            ("something2", '"2"'),
        ],
    )
    def test_exist_object(self, data, key: str, value: str) -> None:
        """Is object in response data."""
        assert {"key": key, "value": value, "read_only": False} in data

    @mark.parametrize(
        "key,value",
        [("something3", '"3"')],
    )
    def test_object_not_exist(self, data, key: str, value: str) -> None:
        """Is object not in response data."""
        assert {"key": key, "value": value, "read_only": False} not in data

    def test_no_public_field_in_api_response(self, data) -> None:
        """User shouldn't see ``public`` field in API response, because it is always True."""
        for row in data:
            assert "public" not in row.keys()


@mark.skip("Feature for this test didn't implemented.")
class TestConfigNotImplemented:
    """Tests for features that was planned, but didn't implemented.

    Todo:
        Implement features and move this tests to ``TestConfig``.
    """

    def test_value_returning_string(self, data) -> None:
        """Check that we returning string, not string in string.

        Example:
            Return ``'abc'`` instead of ``"'abc'"``.
        """
        assert {"key": "something1", "value": "1", "read_only": False} in data
