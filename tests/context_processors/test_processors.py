from autodonate.lib.context_processors import (
    register_variable,
    global_variables,
)


def test_add_global():
    register_variable("TEST", True)
    assert global_variables(None)["TEST"] is True
    register_variable("TEST", "123")
    assert global_variables(None)["TEST"] == "123"
