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
        "admin/index.html",
        context={"title": "Admin"},
    )


def pages(request: HttpRequest) -> HttpResponse:
    """Pages view.

    Args:
        request: The request object.

    Returns:
        response: The response object.
    """
    return render(
        request,
        "admin/pages.html",
        context={"title": "Admin"},
    )
