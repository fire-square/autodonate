"""Stub."""

from autodonate.lib.templatetags.statictags import static


def test_static() -> None:
    """Test static template tag."""
    print(static("test/file"))
    assert isinstance(static("test/file"), str)
