#!/usr/bin/python3
"""This is a Python script that fetches https://alx-intranet.hbtn.io/status"""

from requests import get

if __name__ == "__main__":

    url = 'https://alx-intranet.hbtn.io/status'
    r = get(url, auth=('user', 'pass'))
    the_page = r.text

    print("Body response:\n\t" +
          f"- type: {type(the_page)}\n\t" +
          f"- content: {the_page}"
          )
