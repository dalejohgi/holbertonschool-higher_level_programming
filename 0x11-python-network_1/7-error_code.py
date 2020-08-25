#!/usr/bin/python3
"""Docstring"""

if __name__ == "__main__":
    import requests
    from requests import HTTPError
    from sys import argv
    url = argv[1]
    response = requests.get(url)
    if response:
        content = response.text
        print(content)
    else:
        status_code = response.status_code
        print("Error code: {}".format(status_code))
