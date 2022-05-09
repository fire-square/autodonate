"""Register some tables to the admin panel."""
from django.contrib import admin
from structlog.stdlib import get_logger

from autodonate.models import Config, Donation, Player, Product

log = get_logger()


admin.site.register(Player)
admin.site.register(Donation)
admin.site.register(Product)


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    """Admin Config model."""

    def has_add_permission(self, request, obj=None):
        """Disable add action."""
        log.debug("ConfigAdmin.has_add_permission", request=request, obj=obj)
        return False

    def has_delete_permission(self, request, obj=None):
        """Disable delete."""
        log.debug("ConfigAdmin.has_delete_permission", request=request, obj=obj)
        return False
