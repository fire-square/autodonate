"""Module for manage RCON connection."""

from django.conf import settings
from mcrcon_ipv6 import MCRcon

from autodonate.lib.utils.logger import get_logger

connection: MCRcon = MCRcon(
    settings.CONFIG["RCON_HOST"],
    settings.CONFIG["RCON_PASSWORD"],
    settings.CONFIG.get("RCON_PORT", 25575),
)
log = get_logger(__name__)


class Rcon:
    """Class for manage RCON connection.

    Example:
        In[1]:  Rcon.run("whitelist add Bob")

        Out[2]: 'Added Bob to whitelist'
    """

    @staticmethod
    def run(command: str) -> str:
        """Run command in RCON.

        Args:
            command: Command which to run.

        Returns:
            Server answer.
        """
        global connection

        # noinspection PyBroadException
        try:
            return str(connection.command(command))
        except Exception:
            try:
                connection.connect()
            except Exception as exc:
                log.warning("RCON connection unavailable! Is server offline?")
                raise exc
            return str(connection.command(command))
