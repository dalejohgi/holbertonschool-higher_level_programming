#!/usr/bin/python3
def uppercase(str):
    "Change a string to uppercase"
    for i in range(len(str)):
        if (ord(str[i]) >= 97):
            upper = ord(str[i]) - 32
        else:
            upper = ord(str[i])
        print("{}".format(chr(upper)), end='')
    print()
