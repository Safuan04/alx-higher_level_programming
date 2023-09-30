#!/usr/bin/python3
"""This is a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""

from sys import argv
from urllib.request import urlopen, Request
from urllib.parse import urlencode

if __name__ == "__name__":

    url = argv[1]
    email = argv[2]
    data = urlencode({'email': email}.encode("utf-8"))
    req = Request(url, data=data, method='Post')

    with urlopen(req) as response:
        the_page = response.read()

    print(the_page.decode('URF-8'))
