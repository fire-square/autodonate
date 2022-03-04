from typing import AnyStr, Awaitable, Callable, Union

from aiohttp import web

from autodonate import app, get_logger

log = get_logger(__name__)


def get(path: str, name: Union[None, str] = None):
    log.debug(f'Added GET path "{path}"')

    def get_inner(func: Callable[[web.Request], Awaitable[web.StreamResponse]]):
        app.add_routes([web.get(path, func, name=name)])
        return func

    return get_inner


def post(path: str, name: Union[None, str] = None):
    log.debug(f'Added POST path "{path}"')

    def post_inner(func: Callable[[web.Request], Awaitable[web.StreamResponse]]):
        app.add_routes([web.post(path, func, name=name)])
        return func

    return post_inner


def put(path: str, name: Union[None, str] = None):
    log.debug(f'Added PUT path "{path}"')

    def put_inner(func: Callable[[web.Request], Awaitable[web.StreamResponse]]):
        app.add_routes([web.put(path, func, name=name)])
        return func

    return put_inner


def patch(path: str, name: Union[None, str] = None):
    log.debug(f'Added PATCH path "{path}"')

    def patch_inner(func: Callable[[web.Request], Awaitable[web.StreamResponse]]):
        app.add_routes([web.patch(path, func, name=name)])
        return func

    return patch_inner


def head(path: str, name: Union[None, str] = None):
    log.debug(f'Added HEAD path "{path}"')

    def head_inner(func: Callable[[web.Request], Awaitable[web.StreamResponse]]):
        app.add_routes([web.head(path, func, name=name)])
        return func

    return head_inner


def options(path: str, name: Union[None, str] = None):
    log.debug(f'Added OPTIONS path "{path}"')

    def options_inner(func: Callable[[web.Request], Awaitable[web.StreamResponse]]):
        app.add_routes([web.options(path, func, name=name)])
        return func

    return options_inner


def all_path(path: str, name: Union[None, str] = None):
    log.debug(f'Added all path "{path}"')

    def all_inner(func: Callable[[web.Request], Awaitable[web.StreamResponse]]):
        app.add_routes([web.get(path, func, name=name)])
        app.add_routes([web.post(path, func, name=name)])
        app.add_routes([web.put(path, func, name=name)])
        app.add_routes([web.options(path, func, name=name)])
        app.add_routes([web.patch(path, func, name=name)])
        return func

    return all_inner
