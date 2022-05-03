import imp


import requests
from sys import argv
from glob import glob


for image in glob("screen-*.png"):
    r = requests.post("https://screen.deta.dev/upload",
                    data={"secret": argv[1], "key": argv[2]},
                    files=[open(image, 'rb')])

print(r.json())
