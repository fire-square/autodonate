"""Global cron."""

from typing import Callable
from dataclasses import dataclass
from threading import Thread
from time import sleep, time


@dataclass
class Callback:
    function: Callable[[], None]
    timeout: int
    last_launched: int = 0


callbacks: list[Callback] = []


def register_function(func: Callable[[], None], timeout: int) -> None:
    """Register function in global cron.

    Args:
        func: Function that will be called.
        timeout: Timeout in seconds.
    """
    callback = Callback(function=func, timeout=timeout)
    callbacks.append(callback)


def cron() -> None:
    """Execute functions in cron."""
    while True:
        sleep(1)
        t = int(time())
        for callback in callbacks:
            if t - callback.last_launched >= callback.timeout:
                callback.last_launched = t
                callback.function()


thread = Thread(target=cron)
thread.daemon = True
thread.start()
