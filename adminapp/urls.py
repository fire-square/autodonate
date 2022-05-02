"""URL patterns for index app."""

from django.urls import path

from adminapp.views import *

urlpatterns = [
    path("", index, name="admin-index"),
    path("pages/", pages, name="admin-index")
]
