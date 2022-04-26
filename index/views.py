"""Views module for index app."""

from django.http.request import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    """Render index page."""
    return render(request, "index.html", context={
        "title": "Index",
        "props": {
            "hero": {
                "title": "Лучший маенкрафт сервир",
                "subtitle": "Зайди и праверь!",
                "players": 5
            }
        }
    })
