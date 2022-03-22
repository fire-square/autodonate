from autodonate.plugin_manager import initialize_all
from autodonate.utils.logger import get_logger
from autodonate.app import app


log = get_logger("System")


def setup():
    log.info("Starting PluginManager...")
    initialize_all()
    log.info("PluginManager initialized all.")
