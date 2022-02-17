"""
	Необходимые для работы сайта переменные:
		- SECRET_KEY : переменная задающая ключ шифрования cookie
		- ALLOWED_HOSTS : переменная в формате list:host1.ru,host2.org
							определяет допустимые хедеры "Host"
"""

from os import environ
from pathlib import Path
from toml import load as toml_decode
from json import loads as json_decode
from .lib.utils.logger import get_logger

log = get_logger(__name__)

# Мы создаём BASE_DIR заново, из-за цикличного импортирования
# из settings.py
BASE_DIR = Path(__file__).resolve().parent.parent


class ConfigVariableNotFound(Exception):
    """
    Ошибка, сообщающая о том что переменная не найдена в конфиге.
    Вызывается классом ConfigIntermediate.
    """

    pass


class ConfigNone:
    """
    Класс для отлова ошибок в ConfigIntermediate.__getitem__
    """

    pass


class ConfigIntermediate:
    """
    Класс-прослойка которая пытается прочесть из конфиг
    файла, либо из environ. Environ ограничивает нас в использовании
    вложенных словарей и типов кроме строковых. Мы рассчитываем что
    все необходимые настройки уже есть в конфиге/environ либо задано
    значение по-умолчанию.
    """

    def __init__(self, config: dict | None = None):
        self.config = config

    @staticmethod
    def _process_answer(answer: str):
        """
        Ломаем рамки которые нам дал environ.

        Возможные форматы:
                - json:<json формат>
                - list:<список строк через запятую>
                - bool:<True/False>
                - null:
        """

        if not isinstance(answer, str):
            return answer
        if answer.startswith("json:"):
            return json_decode(answer[5:])
        if answer.startswith("list:"):
            return answer[5:].split(",")
        if answer.startswith("bool:"):
            i = answer[5:].lower()
            if i == "false":
                return False
            elif i == "true":
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
    Класс для доступа к полям конфигурации.
    Неизменяемый.
    """

    def __init__(self):
        # Определяем фнутренние переменные
        self.CONFIG: (dict, None) = None

        # Ищем конфиг
        # Определяем стандартное значение
        self.CONFIG_PATH: Path = BASE_DIR / "config.toml"

        # Если есть "DONATE_CONFIG", используем его
        if (
            environ.get("DONATE_CONFIG")
            and Path(environ.get("DONATE_CONFIG")).is_file()
        ):
            self.CONFIG_PATH: Path = Path(environ.get("DONATE_CONFIG"))

        # Загружаем конфиг
        if not self.CONFIG_PATH.exists():
            log.warn(
                "Файл с конфигом не найден. Укажите "
                "путь до него с помощью переменной "
                "окружения DONATE_CONFIG, либо "
                "добавляйте настройки напрямую в "
                "переменные окружения. Актуальный "
                "конфиг Вы можете получить по ссылке: "
                "https://raw.githubusercontent.com/fire-squad/"
                "autodonate/master/config.toml"
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
                "Основные переменные в конфиге не настроены. "
                "Сайт не может без них работать, обратитесь "
                "за помощью к Вики."
            )
