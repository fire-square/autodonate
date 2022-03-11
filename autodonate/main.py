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
            plugins_module = import_module(plugins_path)
            plugins_module.setup(app, config)
        except ModuleNotFoundError:
            log.error(
                "Plugin `%s` not found. Are you correctly installed it? Check your `pip freeze` and config."
                % plugins_path
            )
        except AttributeError:
            log.error(
                "Plugin `%s` does not provide `setup(app: %s, config: %s)` function."
                % (plugins_path, type(app).__name__, type(config).__name__)
            )
        except TypeError:
            log.error(
                "`setup` function of plugin `%s` possibly has invalid signature. " % plugins_path
                + "Must be `def setup(app: %s, config: %s)`." % (type(app).__name__, type(config).__name__)
            )
