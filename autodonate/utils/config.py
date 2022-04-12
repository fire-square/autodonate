"""File for config classes.

Variables required for the site to work:
    secret_key: a variable that sets the cookie encryption key.

    allowed_hosts: a variable in the "list:host1.ru,host2.org" format defines the allowed "Host" headers.
"""

from json import loads as json_decode
from os import environ
from pathlib import Path
from shutil import copy as copy_file
from typing import Any, Dict, List

from yaml import safe_load as yaml_decode

from autodonate.utils.logger import get_logger

log = get_logger(__name__)

# We are re-creating BASE_DIR due to a circular import
# from settings.py
BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Config:
    """Class for accessing configuration fields."""

    def __init__(self) -> None:
        """__init__ method."""

        # looking for a config
        # determining the default value
        # if there "DONATE_CONFIG" use it
        if environ.get("DONATE_CONFIG") and Path(environ["DONATE_CONFIG"]).is_file():
            self.path: Path = Path(environ["DONATE_CONFIG"])
        else:
            self.path: Path = BASE_DIR / "config.yml"  # type: ignore[no-redef]

        # loading the config
        if self.path.exists():
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
                copy_file(str(BASE_DIR / "config.yml.example"), str(self.path))
                log.warning(f'config.yml.example found, copied to "{self.path}" and used as config')
                self._load()

        self._check()

    def __getitem__(self, config_item: str) -> Any:
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

    def __setitem__(self, key: Any, value: Any) -> None:
        """Idiot-protection.

        Raises:
            TypeError: when idiot detected
        """
        raise TypeError("No. You cant do what.")

    def _load(self) -> None:
        """Load config file."""
        with open(str(self.path), "r") as opened_file:
            self.config: Dict[str, Any] = yaml_decode(opened_file)

    def _check(self) -> None:
        """Checking all necessary variables before starting."""
        if not ("secret_key" in self.config and "allowed_hosts" in self.config):
            log.fatal(
                "The main variables in the config are not configured. "
                + "The site cannot work without them, see Documentation "
                + "(https://autodonate.readthedocs.io/en/latest/) for help.",
            )
            exit(1)

    @staticmethod
    def _process_answer(answer: Any) -> Any:
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

    def get(self, config_item: str, default: Any = None) -> Any:
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
            return self.config[config_item]
        except (ConfigVariableNotFoundError, KeyError) as exception:
            if default is None:
                raise exception
            return default


class ConfigVariableNotFoundError(ValueError):
    """Error reporting that the variable was not found in the config.

    Called by the ConfigIntermediate class.
    """
