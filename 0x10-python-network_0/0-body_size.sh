#!/usr/bin/bash
# this script takes in a URL and displays the body by sending a GET request.
[ -z "$1" ] && { echo "Usage: ./0-body_size.sh <URL>"; exit 1; } ; curl -s "$1" | awk '/^$/{p=0} p; /^c\Content-Length:/{p=1}'
