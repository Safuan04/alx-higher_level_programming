#!/usr/bin/python3
"""Python scrpt that sends a request to a URL and displays the value
of X-Request-Id"""

import urllib.request
from urllib import request
from sys import argv

if __name__ == "__main__":

    try:
        with request.urlopen(argv[1]) as resp:
            headers = resp.headers
            for header, value in headers.items():
                if header == "X-Request-Id":
                    print(headers[header])
    except urllib.error.URLError as e:
        print(e.reason)
