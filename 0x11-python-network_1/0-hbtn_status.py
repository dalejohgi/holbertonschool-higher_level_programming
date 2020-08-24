#!/usr/bin/python3
"""Task 0"""

if __name__ == "__main__":
    from urllib import request
    holb_url = "https://intranet.hbtn.io/status"
    response = request.urlopen(holb_url)
    content = response.read()
    utf8_content = content.decode('utf-8')
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
    print("\t- utf8 content: {}".format(utf8_content))
