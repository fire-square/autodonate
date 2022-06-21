"""Tests for ``/api/player/`` path."""
from json import loads
from typing import Any, Dict, List

from pytest import fixture, mark
from rest_framework.response import Response
from rest_framework.test import APIClient
from structlog import get_logger

from autodonate.models import Player

log = get_logger()

_response: List[Response] = []

parametrize_num: int


def set_up() -> None:
    """Set up some variables for player testing.

    This called once only in ``conftest.py``, do not touch.

    Raises:
        NameError: When ``test_player._response`` variable already set,
            so this function called second time.
    """
    global _response
    if _response != []:
        raise NameError("This function must be called once!")

    for player_nick in ["something1", "something2", "something3"]:
        Player(nickname=player_nick).save()

        _response.append(APIClient().get(f"/api/player/{player_nick}/"))

    _response.append(APIClient().get(f"/api/player/"))


class TestPlayer:
    """Tests for ``/api/player/`` path."""

    @fixture(scope="session", params=[0, 1, 2])
    def response(self, request) -> Response:
        """Response object for parametrizing tests."""
        global parametrize_num
        parametrize_num = request.param
        return _response[parametrize_num]

    def test_status_code(self, response) -> None:
        """``status_code`` must be 200 - okay."""
        assert 200 == response.status_code

    def test_expected_output(self, response) -> None:
        """Is object in response data."""
        assert {"nickname": "something" + str(parametrize_num + 1)} == response.data


class TestPlayerRootPath:
    """Actually, root path of ``/api/player/`` should return 404.

    So in this way, pontential hacker can't get list with all players, he
    will get some info, only if have players nickname, and setted it as
    ``/api/player/{nickname}/``.
    """

    @fixture(scope="session")
    def response(self) -> Response:
        """Actually just return fourth element from ``_response``.

        Becouse fourth element in ``_response`` list is response to API
        root. See ``set_up()`` method here.

        Returns:
            Cached ``Response`` element.
        """
        return _response[3]

    def test_status_code(self, response: Response) -> None:
        """Status code should be 404 here.

        See description of the class.
        """
        assert 404 == response.status_code

    @mark.skip("Feature for this test didn't implemented.")
    def test_status_code_unathorized(self, response: Response) -> None:
        """Status code should be 401 here.

        We should return 401 (Unathorized) instead of just 404 (Not found).

        Todo:
            Implement this, and replace ``test_status_code`` with this test.
        """
        assert 401 == response.status_code
