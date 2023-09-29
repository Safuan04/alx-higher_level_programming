#!/usr/bin/python3
"""Python script that sends a request to a URL and displays the
value of the variable X-Request-Id in the response header"""

import requests
from sys import argv


if __name__ == "__main__":

    req = requests.get(argv[1])
    headers_response = req.headers
    print(headers_response.get("X-Request-Id"))
