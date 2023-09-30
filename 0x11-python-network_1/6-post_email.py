#!/usr/bin/python3
"""This is  a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response."""

from sys import argv
from requests import get, post

if __name__ == "__main__":

    url = argv[1]
    email = argv[2]
    r = post(url, data={'email': email})
    r = get(url, auth=('user', 'pass'))
    print(r.text)
