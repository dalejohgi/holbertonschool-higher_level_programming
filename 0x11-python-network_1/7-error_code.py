#!/usr/bin/python3
"""Docstring"""

if __name__ == "__main__":
    import requests
    from requests import HTTPError
    from sys import argv
    url = argv[1]
    try:
        url = argv[1]
        response = requests.get(url)
        content = response.text
        print(content)
    except HTTPError as e:
        status_code = e.response.status_code
        print("Error code: {}".format(status_code))
