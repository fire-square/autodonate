"""The file is responsible for registering new global variables in templates."""
from typing import Dict, Union

__all__ = ["register_variable", "global_variables"]

VALUES: Dict[str, Union[str, bool]] = {}


def register_variable(name: str, value: Union[str, bool]) -> None:
    """Add a new global variable.

    Args:
        name: variable name (upper case)
        value: variable value
    """
    VALUES[name] = value


def global_variables(request) -> Dict[str, Union[str, bool]]:
    """Return a dictionary of all global variables.

    Called on every render() by Django itself.
    """
    return VALUES
