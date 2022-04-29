"""URL patterns for API app."""

from typing import List

from django.urls import path
from django.urls.resolvers import URLPattern

from api.views import urls

urlpatterns: List[URLPattern] = []

urlpatterns.extend(urls)
