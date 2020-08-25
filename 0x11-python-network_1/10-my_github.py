#!/usr/bin/python3
"""Docstring"""


if __name__ == "__main__":
    import requests
    from sys import argv
    from requests.auth import HTTPBasicAuth
    user = argv[1]
    psswd = argv[2]
    url = "https://api.github.com/users/{}".format(user)
    response = requests.get(url, auth=HTTPBasicAuth(user, psswd))
    my_id = response.json().get('id')
    print(my_id)
