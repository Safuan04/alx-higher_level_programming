#!/bin/bash
# Bash script that sends A Get request to a URL and adds a header to be sent
curl -Hs "X-School-User-Id: 98" "$1"
