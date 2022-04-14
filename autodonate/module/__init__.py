from aiohttp.web import Application, Request, Response, StreamResponse

from autodonate.plugin_models import Plugin, Route
from autodonate.utils.config import Config

__api_version__ = 1


class ExamplePlugin(Plugin):
    pass


def setup(app: Application, config: Config) -> Plugin:
    plugin = ExamplePlugin(app, config)
    return plugin
