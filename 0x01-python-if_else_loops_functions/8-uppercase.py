#!/usr/bin/python3
def uppercase(str):
    "Change a string to uppercase"
    for i in range(len(str)):
        if (ord(str[i]) >= 97):
            print("{}".format(chr(ord(str[i]) - 32)), end='')
        else:
            print("{}".format(str[i]), end='')
    print()
