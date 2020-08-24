#!/usr/bin/python3
"""Docstring"""

if __name__ == "__main__":
    import urllib.request as request
    import urllib.parse as parse
    from sys import argv
    url = argv[1]
    email = argv[2]
    values = {'email': email}
    data = parse.urlencode(values)
    data = data.encode('utf-8')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        content = response.read()
        content = content.decode('utf-8')
        print(content)
