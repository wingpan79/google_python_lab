#! /usr/bin/env python3
import os
import requests
import json
feedback = {}
path = "/data/feedback"
for i in os.listdir(path):
        with open(path+"/{}".format(i)) as f:
                lines = f.read()
                data = lines.splitlines()
                feedback["title"] = data[0]
                feedback["name"] = data[1]
                feedback["date"] = data[2]
                feedback["feedback"] = data[3]
                print(json.dumps(feedback))
                r = requests.post("http://34.135.58.213/feedback/",json = feedback)
                print(r,r.request.body,r.status_code)
