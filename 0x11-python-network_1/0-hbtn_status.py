#!/usr/bin/python3

"""fetches from a given link"""


import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    body = response.read().decode('utf-8')

print('Body response:')
print('\t- type:', type(body))
print('\t- content:', body)
print('\t- utf8 content:', body)
