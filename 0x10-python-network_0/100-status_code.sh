#!/bin/bash
# Sends a requestto a URL and dipslays only the status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
