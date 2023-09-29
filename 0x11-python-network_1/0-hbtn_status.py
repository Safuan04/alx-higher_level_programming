#!/usr/bin/python3
"""importing necessary moduls"""

import urllib.request

if __name__ == "__main__":
    try:
        req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
        with urllib.request.urlopen(req) as response:
            the_page = response.read()

        print("Body response:\n\t" +
              f"- type: {type(the_page)}\n\t" +
              f"- content: {the_page}\n\t" +
              f"- utf8 content: {response.reason}")
    except urllib.error.URLError as e:
        print(e.reason)
