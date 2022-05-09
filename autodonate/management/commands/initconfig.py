"""``initconfig`` command.

This command creates essential command rows.
"""

from django.core.management.base import BaseCommand, CommandError

from autodonate.models import Config


class Command(BaseCommand):
    """Creates essential config rows."""

    def handle(self, *args, **options):
        """Handle ``initconfig`` command."""
        try:
            Config.get("version")
        except Config.DoesNotExist:
            Config.set("version", 0, read_only=True)

        print(f"Version {Config.get('version')}")

        if Config.get("version") < 1:
            print("Version 1")
            Config.set("hero", {"title": "Best server", "subtitle": "Best server ever!"}, public=True)
            Config.set("server", {"ip": "example.com"}, public=True)
            Config.set("version", 1)

        print("Done.")
