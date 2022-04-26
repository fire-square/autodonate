"""``autodonate`` URL Configuration.

The ``urlpatterns`` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/4.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import include, path

from autodonate.settings import DEBUG

urlpatterns = [
    path("", include("index.urls")),
    path("api/", include("api.urls")),
    path("admin/", admin.site.urls),
]

if DEBUG:
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
