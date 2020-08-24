#!/usr/bin/python3
"""Docstring"""


if __name__ == "__main__":
    import requests
    response = requests.get('https://intranet.hbtn.io/status')
    text = response.text
    headers = response.headers
    print(headers.get("X-Request-Id"))
