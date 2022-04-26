"""Modified version of standard Django static templatetag.

The link for static is generated as usual, but the ``ver`` argument
is added to the end with the value ``settings.RUN_ID``.
"""

from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

from django import template
from django.conf import settings
from django.template import Context
from django.template.base import Parser, Token
from django.templatetags.static import PrefixNode
from django.templatetags.static import StaticNode as StaticNodeBase
from django.utils.html import conditional_escape

register = template.Library()


class StaticNode(StaticNodeBase):
    """Modified StaticNode, that adds ``RUN_ID`` to URI."""

    def pre_render(self, context: Context) -> str:
        """Join ``STATIC_URL`` with path."""
        url = self.url(context)
        if context.autoescape:
            url = conditional_escape(url)
        if self.varname is None:
            return str(url)
        context[self.varname] = url
        return ""

    def render(self, context: Context):
        """Join ``STATIC_URL`` with path and add ver argument.

        For internal Django usage.
        """
        url = self.pre_render(context)
        return self.process_url(url)

    @staticmethod
    def process_url(url: str) -> str:
        """Add ver arg to given url.

        Args:
            url: URI

        Returns:
            joined ``url`` with ``?ver=RUN_ID``

        Example: ``https://some.domain/static/path/to/asset.css?ver=543564``
        """
        params = {"ver": settings.RUN_ID}
        url_parts = list(urlparse(url))
        query = dict(parse_qsl(url_parts[4]))
        query.update(params)
        url_parts[4] = urlencode(query)
        return urlunparse(url_parts)


@register.tag("static")
def do_static(parser: Parser, token: Token) -> template.Node:
    """Join the given path with the STATIC_URL setting. For internal Django usage."""
    return StaticNode.handle_token(parser, token)


@register.tag
def get_static_prefix(parser: Parser, token: Token) -> template.Node:
    """Return ``STATIC_URL``."""
    return PrefixNode.handle_token(parser, token, "STATIC_URL")


@register.tag
def get_media_prefix(parser: Parser, token: Token) -> template.Node:
    """Return ``MEDIA_URL``."""
    return PrefixNode.handle_token(parser, token, "MEDIA_URL")


def static(path: str) -> str:
    """Given a relative path to a static asset, return the absolute path to the asset.

    Args:
        path: relative path to asset

    Returns:
        joined path and STATIC_URL

    Example: ``/static/path/to/asset.css?ver=543564``
    """
    return str(StaticNode.handle_simple(path))
