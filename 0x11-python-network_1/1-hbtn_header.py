#!/usr/bin/python3
"""This is a Python script that takes in a URL, sends
a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response."""

from sys import argv
import urllib.request
from urllib.request import urlopen, Request

if __name__ == "__main__":
    url = argv[1]
    req = Request(url)
    with urlopen(req) as response:
        the_page = response.read()
    print(response.headers['X-Request-Id'])
