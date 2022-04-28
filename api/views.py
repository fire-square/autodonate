"""Views module for index app."""

import random

from django.http import HttpRequest, HttpResponse, JsonResponse


def get_latest_donate(request: HttpRequest) -> HttpResponse:
    """Get the latest ticket from the request.

    Args:
        request (HttpRequest): request

    Returns:
        HttpResponse: response
    """
    timestamp = request.GET.get("timestamp")
    if not timestamp or timestamp == "0":
        return JsonResponse(
            {"answer": [{"nick": "test" + str(random.randint(1, 99999)), "item": "крутой меч"} for _ in range(10)]}
        )
    return JsonResponse({"answer": [{"nick": "test" + str(random.randint(1, 99999)), "item": "крутой меч"}]})
