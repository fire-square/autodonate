"""File to automatically create a logger for each file."""

from logging import Formatter, StreamHandler, getLogger, INFO, FileHandler
from pathlib import Path

# We are re-creating BASE_DIR due to a circular import
# from settings.py
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent  # noqa: WPS462


def get_logger(name: str):
    """Method for issuing a personal logger.

    Taken from https://stackoverflow.com/questions/59254843/add-custom-log-records-in-django.
    """  # noqa: E501
    logger = getLogger(name)
    logger.setLevel(INFO)
    file_handler = FileHandler(
        filename="{0}{1}".format(str(BASE_DIR / "logs" / name), ".log"), encoding="utf8",  # noqa: E501
    )
    console_handler = StreamHandler()
    file_formatter = Formatter("%(asctime)s [%(levelname)s] %(message)s")  # noqa: WPS323,E501
    console_formatter = Formatter("[{0}:%(levelname)s] %(message)s".format(name))  # noqa: WPS323,E501
    file_handler.setFormatter(file_formatter)
    console_handler.setFormatter(console_formatter)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger
