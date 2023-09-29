#!/usr/bin/python3
"""importing necessary moduls"""

import urllib.request

if __name__ == "__main__":
    try:
        url = 'https://alx-intranet.hbtn.io/status'
        with urllib.request.urlopen(url) as response:
            the_page = response.read()

        print('Body response:')
        print('    - type:', type(the_page))
        print('    - content:', the_page)
        print('    - utf8 content:', response.reason)
    except urllib.error.URLError as e:
        print(e.reason)
