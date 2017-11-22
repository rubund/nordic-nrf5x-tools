#!/usr/bin/env python3


import sys
import requests

if len(sys.argv) != 3:
    print("Missing arguments")
    sys.exit(-1)

r = requests.post(sys.argv[1], data={"accept_license_agreement" : "accepted"})

status_code = r.status_code

if status_code == 200:
    content = r.content
    fp = open(sys.argv[2], "wb")
    fp.write(content)
    fp.close()
