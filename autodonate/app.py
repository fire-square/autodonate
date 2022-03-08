from aiohttp import web

from autodonate.utils.logger import get_logger

log = get_logger(__name__)


async def handle(request):
    name = request.match_info.get("name", "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


app = web.Application()
app.add_routes([web.get("/", handle), web.get("/{name}", handle)])
