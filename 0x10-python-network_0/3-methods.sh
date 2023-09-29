#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -ls "$1" | awk -F': ' '/Allow/ {print $2}'
