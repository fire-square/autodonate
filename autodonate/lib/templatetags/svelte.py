"""This is code copied from https://github.com/thismatters/django-svelte project.

Modified to not add css files from ``static`` folder.
"""

from typing import Collection, Dict, Optional

from django import template

from autodonate.lib.templatetags.statictags import static

register = template.Library()


@register.inclusion_tag("display_svelte.html")
def svelte(component: str, component_props: Optional[Dict[str, str]] = None) -> Dict[str, Collection[str]]:
    """Handle the display of a Svelte component.

    Args:
        component: Name of ``svelte`` file. Example ``Something.svelte``.
        component_props: The properties to pass to the component. Default {"name": "world"}.

    Returns:
        A dictionary with some keys to handle.
    """
    if component_props is None:
        component_props = {"name": "world"}

    context = {
        "bundle_url": static(f"svelte/{component}.js"),
        "element_id": f"{component}-target",
        "props_name": f"{component}-props",
        "app_name": component,
        "props": component_props,
    }

    return context
