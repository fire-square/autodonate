"""Script for uploading screenshots to public storage."""

from base64 import b64decode
from glob import glob
from sys import argv

import requests


def main(secret_key: str, commit: str) -> str:
    """Main function to upload screenshots.

    Args:
        secret_key: Secret key for uploading. Passing directly to API.
        commit: Commit where screenshot was taken.

    Returns:
        Link to uploaded screenshots.
    """
    for image in glob("screenshot-*.png"):
        response = requests.post(
            "https://screen.deta.dev/upload",
            data={"secret": secret_key, "key": commit, "comment": b64decode(image[11:-4]).decode()},
            files={"file": open(image, "rb")},
        )

    return "https://screen.deta.dev/" + response.json()["key"]


if __name__ == "__main__":
    print(main(argv[1], argv[2]))
