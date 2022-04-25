"""Modified version of standard Django static templatetag.

The link for static is generated as usual, but the ``ver`` argument
is added to the end with the value ``settings.RUN_ID``.
"""

from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

from django import template
from django.conf import settings
from django.templatetags.static import PrefixNode
from django.templatetags.static import StaticNode as StaticNodeBase
from django.utils.html import conditional_escape

register = template.Library()


class StaticNode(StaticNodeBase):
    """Modified StaticNode, that adds ``RUN_ID`` to URI."""

    def pre_render(self, context) -> str:
        """Copied from Django."""
        url = self.url(context)
        if context.autoescape:
            url = conditional_escape(url)
        if self.varname is None:
            return str(url)
        context[self.varname] = url
        return ""

    def render(self, context):
        """Add arg to url and return in to Django.

        From https://stackoverflow.com/questions/2506379/add-params-to-given-url-in-python.
        """
        url = self.pre_render(context)
        return self.process_url(url)

    @staticmethod
    def process_url(url: str) -> str:
        """Add ver arg to given url."""
        params = {"ver": settings.RUN_ID}
        url_parts = list(urlparse(url))
        query = dict(parse_qsl(url_parts[4]))
        query.update(params)
        url_parts[4] = urlencode(query)
        return urlunparse(url_parts)


@register.tag("static")
def do_static(parser, token) -> template.Node:
    """Join the given path with the STATIC_URL setting. For internal Django usage."""
    return StaticNode.handle_token(parser, token)


@register.tag
def get_static_prefix(parser, token):
    """Return ``STATIC_URL``."""
    return PrefixNode.handle_token(parser, token, "STATIC_URL")


@register.tag
def get_media_prefix(parser, token) -> template.Node:
    """Return ``MEDIA_URL``."""
    return PrefixNode.handle_token(parser, token, "MEDIA_URL")


def static(path) -> str:
    """Given a relative path to a static asset, return the absolute path to the asset.

    Args:
        path: relative path to asset

    Returns:
        joined path and STATIC_URL

    Example:
        /static/path/to/asset.css?ver=543564
    """
    return str(StaticNode.handle_simple(path))
