#!/usr/bin/python3
"""Docstring"""

if __name__ == "__main__":
    import requests
    response = requests.get('https://intranet.hbtn.io/status')
    text = response.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
