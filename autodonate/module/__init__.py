from aiohttp.web import Application
from autodonate.utils.config import Config
from autodonate.models import Plugin


class ExamplePlugin(Plugin):
    @


def setup(app: Application, config: Config):
    plugin = ExamplePlugin(app, config)
