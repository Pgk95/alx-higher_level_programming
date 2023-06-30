#!/bin/bash
# this script takes URL as argument and displays the response body by sending GET
curl -sH "X-School-User-Id: 98" "$1"
