"""URL patterns for API app."""

from django.urls import path

from api.views import *

urlpatterns = [path("donate/latest", get_latest_donate, name="get_latest_donate")]
