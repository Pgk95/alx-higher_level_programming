#!/bin/bash
# this script displays all the HTTP methods the server accepts.
curl -sI "$1" | grep" ALLOW" | cut -d " " -f 2-
