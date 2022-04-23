"""Modified version of standard Django static templatetag.

The link for static is generated as usual, but the ``ver`` argument is added to the end with the value ``settings.RUN_ID``.
"""

from urllib.parse import (
    parse_qsl,
    quote,
    urlencode,
    urljoin,
    urlparse,
    urlunparse,
)

from django import template
from django.apps import apps
from django.conf import settings
from django.utils.encoding import iri_to_uri
from django.utils.html import conditional_escape

register = template.Library()


class PrefixNode(template.Node):
    """Copied from Django."""

    def __init__(self, varname=None, name=None):
        """__init__ method."""
        if name is None:
            raise template.TemplateSyntaxError("Prefix nodes must be given a name to return.")
        self.varname = varname
        self.name = name

    @classmethod
    def handle_token(cls, parser, token, name) -> "PrefixNode":
        """Class method to parse prefix node and return a Node."""
        tokens = token.contents.split()
        if len(tokens) > 1 and tokens[1] != "as":
            raise template.TemplateSyntaxError("First argument in '%s' must be 'as'" % tokens[0])
        if len(tokens) > 1:
            varname = tokens[2]
        else:
            varname = None
        return cls(varname, name)

    @classmethod
    def handle_simple(cls, name) -> str:
        """Copied from Django."""
        prefix = str(iri_to_uri(getattr(settings, name, "")))
        return prefix

    def render(self, context):
        """Copied from Django."""
        prefix = self.handle_simple(self.name)
        if self.varname is None:
            return prefix
        context[self.varname] = prefix
        return ""


@register.tag
def get_static_prefix(parser, token):
    """Populate a template variable with the static prefix, ``settings.STATIC_URL``.

    Usage::
        {% get_static_prefix [as varname] %}

    Examples::
        {% get_static_prefix %}
        {% get_static_prefix as static_prefix %}
    """
    return PrefixNode.handle_token(parser, token, "STATIC_URL")


@register.tag
def get_media_prefix(parser, token) -> template.Node:
    """Populate a template variable with the media prefix, ``settings.MEDIA_URL``.

    Usage::
        {% get_media_prefix [as varname] %}

    Examples::
        {% get_media_prefix %}
        {% get_media_prefix as media_prefix %}
    """
    return PrefixNode.handle_token(parser, token, "MEDIA_URL")


class StaticNode(template.Node):
    """Copied from Django."""

    child_nodelists = ()

    def __init__(self, varname=None, path=None):
        """Copied from Django."""
        if path is None:
            raise template.TemplateSyntaxError("Static template nodes must be given a path to return.")
        self.path = path
        self.varname = varname

    def url(self, context) -> str:
        """Copied from Django."""
        path = self.path.resolve(context)
        return self.handle_simple(path)

    def pre_render(self, context) -> str:
        """Copied from Django."""
        url = self.url(context)
        if context.autoescape:
            url = conditional_escape(url)
        if self.varname is None:
            return url
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

    @classmethod
    def handle_simple(cls, path) -> str:
        """Copied from Django."""
        if apps.is_installed("django.contrib.staticfiles"):
            from django.contrib.staticfiles.storage import staticfiles_storage

            return cls.process_url(staticfiles_storage.url(path))
        else:
            return cls.process_url(urljoin(PrefixNode.handle_simple("STATIC_URL"), quote(path)))

    @classmethod
    def handle_token(cls, parser, token) -> "StaticNode":
        """Class method to parse prefix node and return a Node."""
        bits = token.split_contents()

        if len(bits) < 2:
            raise template.TemplateSyntaxError("'%s' takes at least one argument (path to file)" % bits[0])

        path = parser.compile_filter(bits[1])

        if len(bits) >= 2 and bits[-2] == "as":
            varname = bits[3]
        else:
            varname = None

        return cls(varname, path)


@register.tag("static")
def do_static(parser, token) -> template.Node:
    """Join the given path with the STATIC_URL setting.

    Usage::
        {% static path [as varname] %}

    Examples::
        {% static "myapp/css/base.css" %}
        {% static variable_with_path %}
        {% static "myapp/css/base.css" as admin_base_css %}
        {% static variable_with_path as varname %}
    """
    return StaticNode.handle_token(parser, token)


def static(path) -> str:
    """Given a relative path to a static asset, return the absolute path to the asset."""
    return str(StaticNode.handle_simple(path))
