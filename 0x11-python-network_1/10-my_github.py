#!/usr/bin/python3
"""This is a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id"""

import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":

    url = 'https://api.github.com/user'
    username = argv[1]
    pwd = argv[2]

    authentication = HTTPBasicAuth(username=username, password=pwd)

    r = requests.get(url, auth=authentication)

    r_id = r.json().get('id')
    print(r_id)
