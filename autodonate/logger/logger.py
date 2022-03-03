"""File to automatically create a logger for each file."""

from logging import INFO, FileHandler, Formatter, StreamHandler, getLogger
from pathlib import Path


def get_logger(name: str):
    """Method for issuing a personal logger.

    Taken from https://stackoverflow.com/questions/59254843/add-custom-log-records-in-django.
    """
    path = Path("logs")
    path.mkdir(exist_ok=True)
    logger = getLogger(name)
    logger.setLevel(INFO)
    file_handler = FileHandler(
        filename="{0}{1}".format(str(path / name), ".log"),
        encoding="utf8",
    )
    console_handler = StreamHandler()
    file_formatter = Formatter("%(asctime)s [%(levelname)s] %(message)s")
    console_formatter = Formatter("[{0}:%(levelname)s] %(message)s".format(name))
    file_handler.setFormatter(file_formatter)
    console_handler.setFormatter(console_formatter)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger
