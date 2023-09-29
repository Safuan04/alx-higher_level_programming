#!/usr/bin/python3
"""importing necessary moduls"""

if __name__ == "__main__":

    import urllib.request
    try:
        req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
        with urllib.request.urlopen(req) as response:
            the_page = response.read()

        print('Body response:')
        print('    - type:', type(the_page))
        print('    - content:', the_page)
        print('    - utf8 content:', response.reason)
    except urllib.error.URLError as e:
        print(e.reason)
