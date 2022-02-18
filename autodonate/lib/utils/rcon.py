"""Module for manage RCON connection."""

from mcrcon import MCRcon
from autodonate.config import Config


class Rcon:
    """Class for manage RCON connection.

    Example:
        >>> with Rcon().mcr as mcr:
        ...     response = mcr.command("/whitelist add bob")

    Attributes:
        config: Initialized config object.
        mcr: Minecraft RCON connection object.
    """

    __slots__ = ("config", "mcr")

    def __init__(self) -> None:
        """__init__ method."""
        self.config = Config()
        self.mcr = MCRcon(
            self.config["RCON_HOST"],
            self.config["RCON_PASSWORD"],
            self.config.get("RCON_PORT", 25575),
        )
