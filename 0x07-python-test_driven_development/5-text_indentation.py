#!/usr/bin/python3
"""
    Module 5-text_indentation with text_indentation in it
"""


def text_indentation(text):
    """Split a text everytime it finds an special character and prints the lines so far"""
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
