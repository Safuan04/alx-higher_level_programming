#!/usr/bn/python3
"""This is a Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter as a parameter."""

import requests
from sys import argv

if __name__ == "__main__":

    url = 'http://0.0.0.0:5000/search_user'
    q = {'letter': argv[1]}

    r = requests.post(url, json=q)

    print(r.text)
