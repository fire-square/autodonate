"""Register some tables to the admin panel."""
from django.contrib import admin

from autodonate.models import Config

admin.site.register(Config)
