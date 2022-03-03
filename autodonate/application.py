from aiohttp import web
from autodonate import get_logger

log = get_logger(__name__)

app = web.Application()
