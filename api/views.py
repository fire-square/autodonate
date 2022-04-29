"""Views module for index app."""

import random
from string import ascii_lowercase

from django.core.serializers import serialize
from django.http import HttpRequest, HttpResponse, JsonResponse

from autodonate.models import Donation, Product


def get_latest_donate(request: HttpRequest) -> HttpResponse:
    """Get the latest ticket from the request.

    Args:
        request: request

    Returns:
        HttpResponse: response
    """
    donations = [
        Donation(
            product=Product(
                name="Креатив",
                price=100,
            ),
            player_name="".join(random.choices(ascii_lowercase, k=3)),
        )
        for _ in range(10 if request.GET.get("timestamp") == "0" or request.GET.get("timestamp") is None else 1)
    ]
    return JsonResponse(serialize("json", donations), safe=False)
