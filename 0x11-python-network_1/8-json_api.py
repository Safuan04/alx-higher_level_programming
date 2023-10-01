#!/usr/bin/python3
"""This is a Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter as a parameter."""

import requests
from sys import argv

if __name__ == "__main__":

    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]

    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': q}

    try:
        r = requests.post(url, data=payload)
        r_data = r.json()

        if len(r_data) is None:
            print('No result')
        else:
            print(f"[{r_data.get('id')}] {r_data.get('name')}")
    except ValueError:
        print("Not a valid JSON")
