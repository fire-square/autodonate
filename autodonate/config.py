"""Config object for autodonate project. This params set by user."""
from dataclasses import dataclass, field

from structlog.stdlib import get_logger

from autodonate.models import Config

log = get_logger()


@dataclass
class ConfigParams:
    """Config object for autodonate project. This params set by user.

    Do not forget add new fields to migrations.
    """

    project_name: Config = field(default=Config.objects.get("project_name"))

    log.debug("ConfigParams", project_name=project_name)


config = ConfigParams()
