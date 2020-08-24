#!/usr/bin/python3
"""Docstring"""


if __name__ == "__main__":
    import requests
    from sys import argv
    url = argv[1]
    response = requests.get(url)
    text = response.text
    headers = response.headers
    print(headers.get("X-Request-Id"))
