#!/usr/bin/python3

import urllib.request
import urllib.parse
import sys

"""sends a POST request to a given URL with the email."""


def send_post_request(url, email):

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data=data) as response:
        body = response.read().decode('utf-8')

    print(body)


if __name__ == "__main__":

    if len(sys.argv) != 3:
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    send_post_request(url, email)
