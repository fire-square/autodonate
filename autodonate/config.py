"""
    Variables required for the site to work:
        - SECRET_KEY : a variable that sets the cookie encryption key
        - ALLOWED_HOSTS : a variable in the "list:host1.ru,host2.org" format defines the allowed "Host" headers
"""

from os import environ
from pathlib import Path
from toml import load as toml_decode
from json import loads as json_decode
from .lib.utils.logger import get_logger

log = get_logger(__name__)

# We are re-creating BASE_DIR due to a circular import
# from settings.py
BASE_DIR = Path(__file__).resolve().parent.parent


class ConfigVariableNotFound(Exception):
    """
    Error reporting that the variable was not found in the config.
    Called by the ConfigIntermediate class.
    """


class ConfigNone:
    """
    Class for catching errors in Config Intermediate.__getitem__
    """


class ConfigIntermediate:
    """
    An interlayer class that tries to read from a config file, or from environ.
    Environ restricts us from using nested dictionaries and non-string types.
    We expect that all the necessary settings are already in the environ config or the default value is set.
    """

    def __init__(self, config: dict | None = None):
        self.config = config

    @staticmethod
    def _process_answer(answer: str):
        """
        Breaking the boundaries given to us by environ.

        Possible formats:
                - json:<json format>
                - list:<comma separated list of strings>
                - bool:<True/False>
                - null:
        """

        if not isinstance(answer, str):
            return answer
        answer = answer.strip()
        if answer.startswith("json:"):
            return json_decode(answer[5:])
        if answer.startswith("list:"):
            return answer[5:].split(",")
        if answer.startswith("bool:"):
            i = answer[5:].lower()
            if i == "false" or i == "0":
                return False
            elif i == "true" or i == "1":
                return True
        if answer.startswith("null:"):
            return None
        return answer

    def __getitem__(self, item: str):
        if environ.get(item):
            return self._process_answer(environ[item])
        if self.config:
            try:
                return self._process_answer(self.config[item])
            except KeyError:
                raise ConfigVariableNotFound
        raise ConfigVariableNotFound

    def get(self, item: str, default=ConfigNone):
        try:
            return self[item]
        except ConfigVariableNotFound as e:
            if isinstance(default, ConfigNone):
                raise e
            return default


class Config:
    """
    Class for accessing configuration fields. Immutable.
    """

    def __init__(self):
        # defining internal variables
        self.CONFIG: (dict, None) = None

        # looking for a config
        # determining the default value
        self.CONFIG_PATH: Path = BASE_DIR / "config.toml"

        # if there "DONATE_CONFIG" use it
        if environ.get("DONATE_CONFIG") and Path(environ.get("DONATE_CONFIG")).is_file():
            self.CONFIG_PATH: Path = Path(environ.get("DONATE_CONFIG"))

        # loading the config
        if not self.CONFIG_PATH.exists():
            log.warn(
                "The config file was not found. Specify the path to it using the "
                "DONATE_CONFIG environment variable, or add settings directly to "
                "environment variables. You can get the actual config from the link: "
                "https://raw.githubusercontent.com/fire-squad/autodonate/master/config.toml"
            )
        else:
            self._load()

        self.inter: ConfigIntermediate = ConfigIntermediate(config=self.CONFIG)
        self._check()

    def __getitem__(self, item):
        return self.inter[item]

    def get(self, item: str, default=ConfigNone):
        return self.inter.get(item, default)

    def _load(self):
        """
        Загружаем конфиг файл
        """
        with open(str(self.CONFIG_PATH), "r") as file:
            self.CONFIG = toml_decode(file)

    def _check(self):
        try:
            self["SECRET_KEY"]
        except ConfigVariableNotFound:
            log.fatal(
                "The main variables in the config are not configured. The site cannot work without them, "
                "see Wiki for help."
            )
