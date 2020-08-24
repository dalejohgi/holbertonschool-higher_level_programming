#!/usr/bin/python3
"""Docstring"""

if __name__ == "__main__":
    import urllib.request as request
    from urllib.error import HTTPError
    from sys import argv
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            content = response.read()
            content = content.decode('utf-8')
            print(content)
    except HTTPError as e:
        print("Error code: {}".format(e.code))
