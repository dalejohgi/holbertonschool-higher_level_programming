#!/usr/bin/python3
"""Docstring"""


if __name__ == "__main__":
    import requests
    from sys import argv
    q = ""
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) == 2:
        q = argv[1]
    response = requests.post(url, data={'q': q})
    try:
        dic = response.json()
        if dic and dic.get('id') and dic.get('name'):
            print("[{}] {}".format(dic.get('id'), dic.get('name')))
        else:
            print('Not result')
    except:
        print('Not a valid JSON')
