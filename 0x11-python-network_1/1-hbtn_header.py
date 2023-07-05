#!/usr/bin/python3

"""this script takes in a URL sends a
request,get the header of the response"""

import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    x_request_id = response.headers.get('X-request-Id')

print(x_request_id)
