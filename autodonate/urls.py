"""URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/

Examples:
    Function views:
        1. Add an import:  from my_app import views
        2. Add a URL to urlpatterns:  path('', views.home, name='home')

    Class-based views:
        1. Add an import:  from other_app.views import Home
        2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

    Including another URLconf:
        1. Import the include() function: from django.urls import include, path
        2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from autodonate.views import healthcheck


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/health", healthcheck, name="healthcheck"),
]


default_imports = settings.CONFIG.get(
    "URLPATTERNS",
    {"<index>": {"path": "autodonate_placeholder_plugin.urls"}},
)


for entry in default_imports:
    urlpatterns.append(
        path(
            entry.replace("<index>", ""),
            include(default_imports[entry]["path"]),
            name=default_imports[entry].get("name", None),
        )
    )

if settings.CONFIG.get("DEBUG", True) and settings.CONFIG.get(
    "DEBUG_STATICFILES_SERVER", True
):
    urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
