#!/usr/bin/python3
"""this is a  Python script that takes in a URL,
sends a request to the URL and displays the body
of the response (decoded in utf-8)."""

from sys import argv
from urllib.request import urlopen, Request
from urllib.error import HTTPError

if __name__ == "__main__":

    try:
        url = argv[1]
        req = Request(url)
        with urlopen(req) as response:
            the_page = response.read()
        print(the_page.decode('UTF-8'))
    except HTTPError as error:
        print("Error code:", error.code)
