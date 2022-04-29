"""Views module for index app."""


from datetime import datetime

from django.core.serializers import serialize
from django.http import HttpRequest, HttpResponse, JsonResponse

from autodonate.models import Donation, Player, Product


def get_latest_donate(request: HttpRequest) -> HttpResponse:
    """Get the latest ticket from the request.

    Args:
        request: request

    Returns:
        HttpResponse: response
    """
    donations = Donation.objects.filter(date__gt=datetime.fromtimestamp(int(request.GET.get("timestamp", default=0))))
    return HttpResponse(serialize("json", donations), content_type="application/json")


def get_donation(request: HttpRequest) -> HttpResponse:
    """Get donation by id.

    Args:
        request: request

    Returns:
        HttpResponse: response
    """
    return HttpResponse(
        serialize("json", Donation.objects.filter(id=request.GET["id"])), content_type="application/json"
    )


def get_product(request: HttpRequest) -> HttpResponse:
    """Get product information by id.

    Args:
        request: request

    Returns:
        HttpResponse: response
    """
    return HttpResponse(
        serialize("json", Product.objects.filter(id=request.GET["id"])), content_type="application/json"
    )


def get_product_available(request: HttpRequest) -> HttpResponse:
    """Get list of available products.

    Args:
        request: request

    Returns:
        HttpResponse: response
    """
    return HttpResponse(serialize("json", Product.objects.all()), content_type="application/json")
