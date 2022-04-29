"""URL patterns for API app."""

from django.urls import path

from api.views import *

urlpatterns = [
    path("donate/latest", get_latest_donate, name="get_latest_donate"),
    path("get/product", get_product, name="get_product"),
    path("get/product/available", get_product_available, name="get_product_available"),
    path("get/donation", get_donation, name="get_donation"),
]
