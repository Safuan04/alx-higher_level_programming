#!/usr/bin/python3
"""Python script that sends a POST request to the passed URL 
with an email as parameter"""

import urllib.request
from urllib import request, parse
from sys import argv

if __name__ == "__main__":

    try:
        emails = {'email': argv[2]}
        data = parse.urlencode(emails).encode("utf-8")
        req = request.Request(argv[1], data=data, method="POST")
        with request.urlopen(req) as resp:
            resp_data = resp.read().decode("utf-8")
            print(resp_data)
    except urllib.error.URLError as e:
        print(e.reason)
