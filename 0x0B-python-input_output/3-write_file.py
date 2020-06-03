#!/usr/bin/python3
"""Module 3 write_file"""


def write_file(filename="", text=""):
    """Write a string to a text file"""
    with open(filename, 'w', encoding='utf-8') as my_file:
        my_file.write(text)
    with open(filename, encoding='utf-8') as my_file:
        doc = my_file.read()
    return len(doc)
