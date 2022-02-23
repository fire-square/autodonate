"""Tests for autodonate/config.py."""
from autodonate.config import (
    Config,
    ConfigIntermediate,
    ConfigVariableNotFoundError,
)


def test_config_init() -> None:
    """Test for config initialisation."""
    conf = Config()
    assert isinstance(conf, Config)


def test_config_non_existent_variable() -> None:
    """Test for calling config with not existing variable."""
    conf = Config()
    try:
        conf["NON_EXISTENT"]  # noqa: WPS428
    except ConfigVariableNotFoundError:
        return


def test_config_default_value() -> None:
    """Test for checking default value."""
    conf = Config()
    assert conf.get("NON_EXISTENT", True) is True
    assert conf.get("NON_EXISTENT", False) is False
    assert conf.get("NON_EXISTENT", []) == []  # noqa: WPS520
    assert conf.get("NON_EXISTENT", 0) == 0


def test_config_converter() -> None:
    """Test for `ConfigIntermediate._process_answer`."""
    assert ConfigIntermediate._process_answer("list:1,2") == ["1", "2"]
    assert ConfigIntermediate._process_answer("bool:1") is True
    assert ConfigIntermediate._process_answer("bool:0") is False
    assert ConfigIntermediate._process_answer('json:{"key":"value"}') == {"key": "value"}  # noqa: E501
    assert ConfigIntermediate._process_answer("null:") is None
