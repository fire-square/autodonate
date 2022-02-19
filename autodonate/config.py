"""File for config classes.

Variables required for the site to work:
    SECRET_KEY: a variable that sets the cookie encryption key.

    ALLOWED_HOSTS: a variable in the "list:host1.ru,host2.org" format defines the allowed "Host" headers.

    RCON_HOST: Minecraft RCON host (enable-rcon=true in server.properties)

    RCON_PASSWORD: Minecraft RCON password
"""
from os import environ
from shutil import copy as copy_file
from pathlib import Path
from yaml import safe_load as yaml_decode
from json import loads as json_decode
from typing import Any
from autodonate.lib.utils.logger import get_logger

log = get_logger(__name__)

# We are re-creating BASE_DIR due to a circular import
# from settings.py
BASE_DIR = Path(__file__).resolve().parent.parent


class ConfigVariableNotFoundError(Exception):
    """Error reporting that the variable was not found in the config.

    Called by the ConfigIntermediate class.
    """


class ConfigNone(object):
    """Class for catching errors in Config Intermediate.__getitem__."""


class ConfigIntermediate(object):
    """An interlayer class that tries to read from a config file, or from environ.

    Environ restricts us from using nested dictionaries
    and non-string types.

    We expect that all the necessary settings are already
    in the environ config or the default value is set.
    """

    def __init__(self, config: dict[str, object] | None = None) -> None:
        """__init__ method.

        Args:
            config: Config in a dict.
        """
        self.config = config

    def __getitem__(self, config_item: str) -> Any:  # type: ignore[misc]
        """Make config accessible by `Config["Value"]`.

        Args:
            config_item: Item used in `Config[item]`

        Returns:
            Parsed result from environ or config.

        Raises:
            ConfigVariableNotFoundError: When config variable not found,
                or when `self.config` not set.
        """
        if environ.get(config_item):
            return self._process_answer(environ[config_item])

        if self.config:
            try:
                return self._process_answer(self.config[config_item])
            except KeyError:
                raise ConfigVariableNotFoundError("Config variable not found.")

        raise ConfigVariableNotFoundError("`self.config` is not set.")

    def get(self, config_item: str, default: Any = ConfigNone) -> Any:  # type: ignore[misc]
        """Return the value for key if key is in the dictionary, else default.

        Args:
            config_item: Item to get from `self`.
            default: Default value for config_item.

        Returns:
            Value from config, or if it not exists, value from `default`.

        Raises:
            ConfigVariableNotFoundError: When config variable not found.
        """
        try:
            return self[config_item]
        except ConfigVariableNotFoundError as exception:
            if isinstance(default, ConfigNone):
                raise exception
            return default

    @staticmethod
    def _process_answer(answer: object) -> Any:  # type: ignore[misc]
        """Breaking the boundaries given to us by environ.

        Args:
            answer: Answer from environ.

                Possible formats:
                    - json:<json format>
                    - list:<comma separated list of strings>
                    - bool:<True/False>
                    - null:

        Returns:
            Parsed answer from environ.
        """
        if not isinstance(answer, str):
            return answer

        answer = answer.strip()
        if answer.startswith("json:"):
            return dict(json_decode(answer[5:]))

        elif answer.startswith("list:"):
            return answer[5:].split(",")

        elif answer.startswith("bool:"):
            return bool(int(answer[5:]))

        elif answer.startswith("null:"):
            return None

        return answer


class Config(object):
    """Class for accessing configuration fields. Immutable."""

    def __init__(self) -> None:
        """__init__ method."""
        self.CONFIG: dict[str, object] | None = None

        # looking for a config
        # determining the default value
        # if there "DONATE_CONFIG" use it
        if environ.get("DONATE_CONFIG") and Path(environ["DONATE_CONFIG"]).is_file():
            self.CONFIG_PATH: Path = Path(environ["DONATE_CONFIG"])
        elif Path("/config/config.yml").is_file():
            self.CONFIG_PATH: Path = Path("/config/config.yml")  # type: ignore[no-redef]
        else:
            self.CONFIG_PATH: Path = BASE_DIR / "config.yml"  # type: ignore[no-redef]

        # loading the config
        if self.CONFIG_PATH.exists():
            self._load()
        else:
            log.warning(
                "The config file was not found. Specify the path to it using "
                + "the DONATE_CONFIG environment variable, or add settings "
                + "directly to environment variables. You can get the actual "
                + "config from the link: "
                + "https://raw.githubusercontent.com/fire-squad/autodonate/master/config.yml.example",
            )
            if (BASE_DIR / "config.yml.example").is_file():
                copy_file(str(BASE_DIR / "config.yml.example"), str(self.CONFIG_PATH))
                log.warning(
                    'config.yml.example found, copied to "%s" and used '
                    % str(self.CONFIG_PATH)
                    + "as config"
                )
                self._load()

        self.inter: ConfigIntermediate = ConfigIntermediate(config=self.CONFIG)
        self._check()

    def __getitem__(self, config_item: str) -> Any:  # type: ignore[misc]
        """Make object accessible same as list.

        Args:
            config_item: Item to return from config.

        Returns:
            Value from config, with key `config_item`.
        """
        return self.inter[config_item]

    def get(self, config_item: str, default: Any = ConfigNone) -> Any:  # type: ignore[misc]
        """Return the value for key if key is in the dictionary, else default.

        Args:
            config_item: Item to get from `self`.
            default: Default value for config_item.

        Returns:
            Value from config, with key `config_item`.

            If there is no value in config, returns value from `default`.
        """
        return self.inter.get(config_item, default)

    def _load(self) -> None:
        """Load config file."""
        with open(str(self.CONFIG_PATH), "r") as opened_file:
            self.CONFIG = yaml_decode(opened_file)

    def _check(self) -> None:
        """Checking all necessary variables before starting."""
        try:
            self["SECRET_KEY"]
            self["ALLOWED_HOSTS"]
            self["RCON_HOST"]
            self["RCON_PASSWORD"]
        except ConfigVariableNotFoundError:
            log.fatal(
                "The main variables in the config are not configured. "
                + "The site cannot work without them, see Documentation "
                + "(https://autodonate.readthedocs.io/en/latest/) for help.",
            )
            exit(1)
