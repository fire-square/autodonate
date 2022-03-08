"""File to automatically create a logger for each file."""

from logging import (
    CRITICAL,
    DEBUG,
    INFO,
    FileHandler,
    Formatter,
    StreamHandler,
    getLogger,
)
from os import environ
from pathlib import Path

__all__ = ["get_logger"]


def get_logger(name: str):
    """Method for issuing a personal logger.

    Taken from https://stackoverflow.com/questions/59254843/add-custom-log-records-in-django.
    """
    path = Path(environ.get("LOG_PATH", "logs"))
    path.mkdir(exist_ok=True)
    logger = getLogger(name)
    log_level = environ.get("LOG_LEVEL", "INFO").upper()
    log_separate = bool(int(environ.get("LOG_SEPARATE", 0)))

    if log_level == "DEBUG":
        logger.setLevel(DEBUG)
    elif log_level == "CRITICAL":
        logger.setLevel(CRITICAL)
    else:
        logger.setLevel(INFO)

    file_handler = FileHandler(
        filename="{0}.log".format(str(path / (name if log_separate else "autodonate"))),
        encoding="utf8",
    )
    console_handler = StreamHandler()
    file_formatter = Formatter("%(asctime)s [{0}:%(levelname)s] %(message)s".format(name))
    console_formatter = Formatter("[{0}:%(levelname)s] %(message)s".format(name))
    file_handler.setFormatter(file_formatter)
    console_handler.setFormatter(console_formatter)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger
