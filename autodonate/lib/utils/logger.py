"""
    File to automatically create a logger for each file.
"""

import logging
from pathlib import Path

# We are re-creating BASE_DIR due to a circular import
# from settings.py
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent


# taken from https://stackoverflow.com/questions/59254843/add-custom-log-records-in-django
def get_logger(name: str):
    """
    Method for issuing a personal logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(
        filename=str(BASE_DIR / "logs" / name) + ".log", encoding="utf8"
    )
    console_handler = logging.StreamHandler()
    file_formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    console_formatter = logging.Formatter(f"[{name}:%(levelname)s] %(message)s")
    file_handler.setFormatter(file_formatter)
    console_handler.setFormatter(console_formatter)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger
