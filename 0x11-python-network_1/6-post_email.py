#!/usr/bin/python3
"""Docstring"""


if __name__ == "__main__":
    import requests
    from sys import argv
    url = argv[1]
    email = argv[2]
    queries = {'email': email}
    response = requests.post(url, data=queries)
    print(response.text)
