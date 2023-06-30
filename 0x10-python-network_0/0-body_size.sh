#!/usr/bin/bash
# this script takes in a URL and displays the body by sending a GET request.
curl-s "$1" | wc -c
