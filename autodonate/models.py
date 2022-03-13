from autodonate.utils.logger import get_logger
from autodonate.utils.config import Config
from abc import ABCMeta, abstractmethod
from typing import Optional, Callable, Awaitable
from aiohttp import web


class Base:
    """Base class, in order not to duplicate the initialization code of the config, application, logger."""

    def __init__(self, app: web.Application, config: Config) -> None:
        """__init__ method.

        Arguments:
            app: Application instance
            config: Config instance
        """
        self.app = app
        self.config = config
        self.log = get_logger(self.__class__.__name__)


class Route(Base):
    def __init__(self, *args, name: str) -> None:
        super().__init__(*args)
        self.name = name

        # getting base path from config. using content of routes.{name}, or "/{name}" if not found
        self.base_path = self.config.get("routes", {}).get(name, f"/{name}")
        self.log.debug(f"Using `%s` base path for plugin `%s`" % (self.base_path, self.name))

    def get(self, path: str, name: Optional[str] = None, absolute: bool = False):
        self.log.debug(f'Added GET path "{path}"')

        def get_inner(func: Callable[[web.Request], Awaitable[web.StreamResponse]]):
            self.app.add_routes([web.get(self.base_path+path if absolute else path, func, name=name)])
            return func

        return get_inner


class Plugin(Base, metaclass=ABCMeta):
    def __init__(self, *args) -> None:
        super().__init__(*args)
        self.route = Route(self.app, self.config, name=self.__class__.__name__)
