from autodonate.utils.config import Config
from autodonate.app import app
from autodonate.utils.logger import get_logger
from importlib import import_module


log = get_logger("PluginManager")


def initialize_all() -> None:
    """Initialize system and all plugins."""

    config = Config()
    for plugins_path in config["plugins"]:
        try:
            log.info("Enabling `%s`..." % plugins_path)
            plugins_module = import_module(plugins_path)
            if "setup" in plugins_module.__dir__():
                if plugins_module.__api_version__ != 1:
                    log.fatal("Unsupported version.")
                    exit(1)
                plugins_module.setup(app, config)
            else:

                # Some checking to help end developer
                for name in [item for item in dir(plugins_module) if not item.startswith("_")]:
                    if name.endswith("Plugin") and name != "Plugin":
                        log.fatal(f"Module {plugins_path} provides a Plugin `{name}`, "
                                       f"but does not have a `setup()` function to initialize it.")
                        exit(1)
                log.fatal(f"Module {plugins_path} doesn't provides a Plugin.")
                exit(1)

            log.info("Enabled `%s`." % plugins_path)
        except ModuleNotFoundError as exception:
            log.error(
                "Plugin `%s` not found. Are you correctly installed it? "
                "Check your `pip freeze` output and config. (Error: %s)"
                % (plugins_path, exception)
            )
        except AttributeError as exception:
            log.error(
                "Plugin `%s` does not provide `setup(app: %s, config: %s)` function. (Error: %s)"
                % (plugins_path, type(app).__name__, type(config).__name__, exception)
            )
        except TypeError as exception:
            log.error(
                "`setup` function of plugin `%s` possibly has invalid signature. " % plugins_path
                + "Must be `def setup(app: %s, config: %s) -> Plugin`. Error: `%s`" %
                (type(app).__name__, type(config).__name__, exception)
            )
