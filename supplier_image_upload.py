#!/usr/bin/env python3

import os
import requests

url = "http://localhost/upload/"
path = "supplier-data/images/"

for file in os.listdir(path):
    if ".jpeg" in file:
        with open(path + file, 'rb') as opened:
            r = requests.post(url, files={'file': opened})




