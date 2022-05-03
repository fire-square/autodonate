"""Script for uploading screenshots to public storage."""

from glob import glob
from sys import argv
from urllib.parse import unquote_plus

import requests

for image in glob("Screenshot*.png"):
    r = requests.post(
        "https://screen.deta.dev/upload",
        data={"secret": argv[1], "key": argv[2], "comment": unquote_plus(image)},
        files={"file": open(image, "rb")},
    )

print("https://screen.deta.dev/" + r.json()["key"])
