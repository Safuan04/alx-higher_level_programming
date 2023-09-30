#!/usr/bin/python3
"""This is  a Python script that takes in a URL,
sends a request to the URL and displays the body of the response."""

from sys import argv
from requests import get

if __name__ == "__main__":

    url = argv[1]
    r = get(url, auth=('user', 'pass'))
    stat_code = r.status_code

    if stat_code >= 400:
        print("Error code:", stat_code)