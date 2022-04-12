from autodonate.utils.logger import get_logger
from autodonate.utils.config import Config
from abc import ABCMeta
from typing import Optional, Callable, Awaitable
from aiohttp import web
from aiohttp.web import Request, Response


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
        """Initialize Route system for plugin.

        Args:
            *args: args of Base class
            name: name used to search paths in config
        """
        super().__init__(*args)
        self.name = name

        # getting base path from config. using content of routes.{name}, or "/{name}" if not found
        self.base_path = self.config.get("routes", {}).get(name, f"/{name}")
        self.log.debug(f"Using `%s` base path for plugin `%s`" % (self.base_path, self.name))

    def get(self, func: Callable[[web.Request], Awaitable[web.StreamResponse]], path: str,
            name: Optional[str] = None, absolute: bool = False) -> None:
        """Add method to global routing.

        Args:
            func: view method of plugin
            path: relative (or absolute) path
            name: global name for using resolving in templates
            absolute: indicates whether the link is absolute, or you need to use the config to determine the path

        Returns:
            None
        """
        self.log.debug(f'Added GET path `{path}` as `{self.base_path}/{path}` to method `{str(func)}`')
        self.app.add_routes([web.get(path if absolute else self.base_path+'/'+path, func, name=name)])

    # TODO: Decorator support (maybe impossible)
    # TODO: PROBLEM: Decorator can't access content of method.__self__, because object not initialized.
    # TODO: PROBLEM: Or more precisely: when we use a decorator on a method, we get a function that does
    # TODO: PROBLEM: not know anything from the parent.
    #
    # def _get(self, func: Callable[[web.Request], Awaitable[web.StreamResponse]], path: str,
    #         name: Optional[str] = None, absolute: bool = False) -> None:
    #     self.log.debug(f'Added GET path `{path}` as `{self.base_path}/{path}` to method `{str(func)}`')
    #     self.app.add_routes([web.get(path if absolute else self.base_path+'/'+path, func, name=name)])
    #
    # @staticmethod
    # def get(path: str, name: Optional[str] = None, absolute: bool = False):
    #     def get_inner(func: Callable[[web.Request], Awaitable[web.StreamResponse]]):
    #         method_object = func.__self__
    #         self = Route(method_object.app, method_object.config, name=method_object.name)
    #         self._get(func=func, path=path, name=name, absolute=absolute)
    #         return func
    #     return get_inner


class Plugin(Base, metaclass=ABCMeta):
    def __init__(self, *args) -> None:
        """Initialize plugin, and Route for them.

        Args:
            *args: args of Base class
        """
        super().__init__(*args)
        self.name = self.__class__.__name__
        self.route = Route(self.app, self.config, name=self.name)
        self.setup_routes()

    def setup_routes(self) -> None:
        """Setup routes to views.

        Examples:
            self.route.get(self.index_view, '')

        Returns:
            None
        """
        self.route.get(self.index_view, '')

    async def index_view(self, request: Request) -> Response:
        return Response(text=f"Plugin {self.name} initialized! "
                             f"Now create custom views and register it in setup_routes method.")
