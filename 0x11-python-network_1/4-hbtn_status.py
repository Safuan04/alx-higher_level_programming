#!/usr/bin/python3
"""Python script that fetches a URL using the package requests"""

import requests

if __name__ == "__main__":

    req = requests.get("https://alx-intranet.hbtn.io/status")
    the_page = req.text
    print("Body response:\n\t" +
          f"- type: {type(the_page)}\n\t" +
          f"- content: {the_page}")
