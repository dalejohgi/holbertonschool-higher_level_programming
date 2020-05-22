#!/usr/bin/python3
"""
    Here goes the modules docstring
"""


def text_indentation(text):
    if type(text) is not str:
        raise TypeError('text must be a string')
    line = ""
    for character in text:
        if line == "" and character is " ":
            continue
        elif character not in ["?", ".", ":"]:
            line = line + character
        else:
            print(line + "\n")
            line = ""
