from autodonate.utils.config import Config
from autodonate.app import app
from autodonate.utils.logger import get_logger
from aiohttp import web
from importlib import import_module


log = get_logger(__name__)


def initialize() -> None:
    """Initialize system and all plugins."""

    config = Config()
    for plugins_path in config["plugins"]:
        try:
            log.info("Enabling `%s`..." % plugins_path)
            plugins_module = import_module(plugins_path)
            plugins_module.setup(app, config)
            log.info("Enabled `%s`." % plugins_path)
        except ModuleNotFoundError as e:
            log.error(
                "Plugin `%s` not found. Are you correctly installed it? Check your `pip freeze` and config. (Error: %s)"
                % (plugins_path, e)
            )
        except AttributeError as e:
            log.error(
                "Plugin `%s` does not provide `setup(app: %s, config: %s)` function. (Error: %s)"
                % (plugins_path, type(app).__name__, type(config).__name__, e)
            )
        except TypeError as e:
            log.error(
                "`setup` function of plugin `%s` possibly has invalid signature. " % plugins_path
                + "Must be `def setup(app: %s, config: %s)`. (Error: %s)" % (type(app).__name__, type(config).__name__, e)
            )
