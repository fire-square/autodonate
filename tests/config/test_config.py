"""Tests for autodonate/config.py"""
from autodonate.config import Config, ConfigVariableNotFound, ConfigIntermediate


def test_config_init() -> None:
    conf = Config()
    assert isinstance(conf, Config)


def test_config_non_existent_variable() -> None:
    conf = Config()
    try:
        conf["NON_EXISTENT"]
    except ConfigVariableNotFound as e:
        return None


def test_config_default_value() -> None:
    conf = Config()
    assert conf.get("NON_EXISTENT", True) is True
    assert conf.get("NON_EXISTENT", False) is False
    assert conf.get("NON_EXISTENT", []) == []
    assert conf.get("NON_EXISTENT", 0) == 0


def test_config_converter() -> None:
    assert ConfigIntermediate._process_answer("list:1,2") == ["1", "2"]
    assert ConfigIntermediate._process_answer("bool:1") is True
    assert ConfigIntermediate._process_answer("bool:true") is True
    assert ConfigIntermediate._process_answer("bool:0") is False
    assert ConfigIntermediate._process_answer("bool:false") is False
    assert ConfigIntermediate._process_answer('json:{"key":"value"}') == {
        "key": "value"
    }
    assert ConfigIntermediate._process_answer("null:") is None
