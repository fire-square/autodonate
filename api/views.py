"""Views module for index app."""


from datetime import datetime
from typing import List

from django.core.serializers import serialize
from django.http import HttpRequest, JsonResponse
from django.urls.resolvers import URLPattern

from autodonate.models import Donation, Product
from autodonate.views import route

urls: List[URLPattern] = []


@route("donate/latest", urls)
def get_latest_donate(request: HttpRequest) -> JsonResponse:
    """Get the latest ticket from the request.

    Args:
        request: request

    Returns:
        response
    """
    donations = Donation.objects.filter(date__gt=datetime.fromtimestamp(int(request.GET.get("timestamp", default=0))))
    return JsonResponse(serialize("python", donations))


@route("get/donation", urls)
def get_donation(request: HttpRequest) -> JsonResponse:
    """Get donation by id.

    Args:
        request: request

    Returns:
        response
    """
    return JsonResponse(serialize("python", Donation.objects.filter(id=request.GET["id"])))


@route("get/product", urls)
def get_product(request: HttpRequest) -> JsonResponse:
    """Get product information by id.

    Args:
        request: request

    Returns:
        response
    """
    return JsonResponse(serialize("python", Product.objects.filter(id=request.GET["id"]))[0])


@route("get/product/available", urls)
def get_product_available(request: HttpRequest) -> JsonResponse:
    """Get list of available products.

    Args:
        request: request

    Returns:
        response
    """
    return JsonResponse(serialize("python", Product.objects.all()), safe=False)
