"""Some standart methods for `views.py`."""
from typing import Callable, List

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.urls import path as djpath
from django.urls.resolvers import URLPattern

#: Type of the decorated function. See sources.
decorated_function_type = Callable[[HttpRequest], HttpResponse]


def route(path: str, urls: List[URLPattern], **kwargs) -> Callable[[decorated_function_type], None]:
    """Route the path, use this as decorator.

    Example:
        .. code-block:: python

            # views.py
            from django.urls.resolvers import URLPattern

            urls: List[URLPattern] = []

            @route("/info", urls)
            def get_info(request: HTTPRequest -> HttpResponse:
                ...

        .. code-block:: python

            # urls.py
            from your_app.views import urls
            ...
            urlpatterns.extend(urls)

    Args:
        path: Path to which we need register function.
        urls: List with your URLs, to which we need append function.
        kwargs: Some options passed directly to ``django.urls.path``.

    Returns:
        Wrapper that will handle register your function.
    """

    def wrapper(func: decorated_function_type) -> None:
        """Wrapper for a function.

        Args:
            func: Your function. This is auto inputted by Python decorator system.
        """
        path_name = path or func.__name__
        urls.append(djpath(path_name, func, **kwargs))

    return wrapper
