#!/usr/bin/env python3
import requests
import glob
# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
for file in glob.glob("supplier-data/images/*.jpeg"):
        with open(file, 'rb') as opened:
                r = requests.post(url, files={'file': opened})
