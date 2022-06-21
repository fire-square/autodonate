"""Tests for ``/api/product/`` path."""
from json import loads
from typing import Any, Dict, List

from pytest import fixture, mark
from rest_framework.response import Response
from rest_framework.test import APIClient
from structlog import get_logger

from autodonate.models import Product

log = get_logger()

response: Response = None

products: List[Product] = []


def get_fields(num: int, enabled: bool, returning: bool = False) -> Dict[str, Any]:  # type: ignore[misc] # explicit any
    """Return dict with keys which need to be passed in model.

    Args:
        num: Custom unique number of row.
        enabled: Is row enabled?
        returning: Return dict which would be returned in API.

    Returns:
        Dict which needs to be unpacked with **.

    Example:
        .. code-block: python

            from autodonate.models import Product
            Product(**get_fields(1, True))
    """
    to_return = {
        "id": str(num),
        "name": "something" + str(num),
        "price": 123,
        "long_description": "long description",
        "group": "test",
        "image": "image",
        "max_in_cart": num,
        "enabled": enabled,
    }

    if returning:
        to_return["image"] = "http://testserver/media/image"
        to_return.pop("enabled")

    return to_return


def set_up() -> None:
    """Set up some variables for product testing.

    This called once only in ``conftest.py``, do not touch.

    Raises:
        NameError: When ``test_product.response`` variable already set,
            so this function called second time.
    """
    # Add some fields in DB
    global products
    for fields in [get_fields(1, True), get_fields(2, True), get_fields(3, False)]:
        product = Product(**fields)
        products.append(product)
        product.save()

    # Get and cache `Response` object
    global response
    if response is not None:
        raise NameError("This function must be called once!")
    response = APIClient().get("/api/product/")


class TestProduct:
    """Tests for ``/api/product/`` path."""

    @fixture(scope="session")
    def data(self):
        """Parse and return dict with answer."""
        return loads(response.content)

    def test_status_code(self) -> None:
        """``status_code`` must be 200 - okay."""
        assert 200 == response.status_code

    @mark.parametrize("num", [1, 2])
    def test_exist_object(self, data, num: int) -> None:
        """Is object in response data."""
        assert get_fields(num, True, True) in data

    @mark.parametrize("num", [3])
    def test_object_not_exist(self, data, num: int) -> None:
        """Is object not in response data."""
        assert get_fields(num, False, True) not in data

    def test_no_enabled_field_in_api_response(self, data) -> None:
        """User shouldn't see ``enabled`` field in API response, because it is always True."""
        for row in data:
            assert "enabled" not in row.keys()
