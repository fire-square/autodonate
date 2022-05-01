"""This is code copied from https://github.com/thismatters/django-svelte project.

Modified to not add css files from ``static`` folder.
"""

from typing import Dict, Optional

from django import template
from django.contrib.staticfiles.storage import staticfiles_storage

register = template.Library()


@register.inclusion_tag("display_svelte.html")
def display_svelte(component: str, component_props: Optional[Dict[str, str]] = None) -> Dict[str, str]:
    """Handle the display of a Svelte component.

    Args:
        component: Name of ``svelte`` file. Example ``Something.svelte``.
        component_props: The properties to pass to the component. Default {"name": "world"}.

    Returns:
        A dictionary with some keys to handle.
    """
    if component_props is None:
        component_props = {"name": "world"}

    if not component.endswith(".svelte"):
        raise ValueError("component name should end with '.svelte'")

    app_name = component[:-7]

    context = {
        "bundle_url": staticfiles_storage.url(f"{app_name}.js"),
        # Line below was deleted.
        # "css_bundle_url": staticfiles_storage.url(f"{app_name}.css"),
        "element_id": f"{app_name.lower()}-target",
        "props_name": f"{app_name.lower()}-props",
        "app_name": app_name,
        "props": component_props,
    }

    return context
