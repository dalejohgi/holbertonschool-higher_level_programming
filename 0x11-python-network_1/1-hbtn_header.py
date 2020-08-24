#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id"""

if __name__ == "__main__":
    import urllib.request as request
    from sys import argv
    holb_url = argv[1]
    with request.urlopen(holb_url) as response:
        print(response.headers.get("X-Request-Id"))
