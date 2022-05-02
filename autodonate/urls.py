"""``autodonate`` URL Configuration.

The ``urlpatterns`` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/4.0/topics/http/urls/
"""

from decouple import config
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin as django_admin
from django.urls import include, path

from autodonate.settings import DEBUG

urlpatterns = [
    path("", include("index.urls")),
    path("api/", include("api.urls")),
    path(config("ADMIN_URL", default="admin/"), include("adminapp.urls")),
    path(config("DJANGO_ADMIN_URL", default="django-admin/"), django_admin.site.urls),
]

if DEBUG:
    # Stub for debug_toolbar
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))

    # Serve user-uploaded media files for debug mode
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#: Rename admin panel elements
django_admin.site.site_title = "autodonate"
django_admin.site.site_header = "Admin panel"
django_admin.site.index_title = "autodonate"
