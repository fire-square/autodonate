"""Views module for index app."""

import random
from string import ascii_lowercase

from django.http import HttpRequest, HttpResponse, JsonResponse

from api.structures import Donation, LatestDonates, Player


def get_latest_donate(request: HttpRequest) -> HttpResponse:
    """Get the latest ticket from the request.

    Args:
        request (HttpRequest): request

    Returns:
        HttpResponse: response
    """
    donations = [
        Donation(
            id=random.randint(0, 999),
            name="Креатив",
            price=100,
            player=Player(nick="".join(random.choices(ascii_lowercase, k=3))),
        )
        for i in range(10 if request.GET.get("timestamp") == "0" or request.GET.get("timestamp") is None else 1)
    ]
    return JsonResponse(LatestDonates(donates=donations).to_dict())
