"""Views module for index app."""

import random
from string import ascii_lowercase

from django.core.serializers import serialize
from django.http import HttpRequest, HttpResponse, JsonResponse

from autodonate.models import Donation, Product, Player
from datetime import datetime

def get_latest_donate(request: HttpRequest) -> HttpResponse:
    """Get the latest ticket from the request.

    Args:
        request: request

    Returns:
        HttpResponse: response
    """
    donations = Donation.objects.filter(date__gt=datetime.fromtimestamp(int(request.GET.get('timestamp', default=0))))
    return HttpResponse(serialize("json", donations), content_type="application/json")
