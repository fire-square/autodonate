"""Views module for index app."""

from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """Index view.

    Args:
        request: The request object.

    Returns:
        response: The response object.
    """
    return render(
        request,
        "index.html",
        context={
            "title": "Index",
            "props": {
                "hero": {
                    "title": "Лучший сервер",
                    "subtitle": "Майнкрафт сервер для легенд",
                    "players": 5,
                    "ip": "example.com",
                }
            },
        },
    )
