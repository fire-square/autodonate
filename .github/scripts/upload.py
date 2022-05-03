"""Script for uploading screenshots to public storage."""

from base64 import b64decode
from glob import glob
from sys import argv

import requests

for image in glob("Screenshot*.png"):
    r = requests.post(
        "https://screen.deta.dev/upload",
        data={"secret": argv[1], "key": argv[2], "comment": b64decode(image[11:-4]).decode()},
        files={"file": open(image, "rb")},
    )

print("https://screen.deta.dev/" + r.json()["key"])
