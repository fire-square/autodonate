"""Remove residual trash generated with `sphinx`."""
from glob import glob
from os import remove


def remove_trash():
    """Remove residual trash generated with `sphinx`."""
    for file in glob("modules/autodonate*.rst"):
        remove(file)


if __name__ == "__main__":
    remove_trash()
