"""
	Файл для автоматического создания логгера
	под каждый файл.
"""

import logging
from pathlib import Path

# Мы создаём BASE_DIR заново, из-за цикличного импортирования
# из settings.py
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent


# Взято из https://stackoverflow.com/questions/59254843/add-custom-log-records-in-django
def get_logger(name: str):
    """
    Метод для выдачи персонального логгера.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(
        filename=str(BASE_DIR / "logs" / (name + ".log")), encoding="utf8"
    )
    console_handler = logging.StreamHandler()
    file_formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    console_formatter = logging.Formatter(f"[{name}:%(levelname)s] %(message)s")
    file_handler.setFormatter(file_formatter)
    console_handler.setFormatter(console_formatter)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger
