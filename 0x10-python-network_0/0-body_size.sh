#!/bin/bash
# Bash script that takes in a URL and displays the size of the body of the response
curl -Is "$1" | awk -F': ' '/Content-Length/ {print $2}'
