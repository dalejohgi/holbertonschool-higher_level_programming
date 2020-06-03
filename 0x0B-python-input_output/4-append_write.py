#!/usr/bin/python3
def append_write(filename="", text=""):
    """Append a string to a text file"""
    with open(filename, 'a', encoding='utf-8') as my_file:
        my_file.write(text)
    with open(filename, encoding='utf-8') as my_file:
        doc = my_file.read()
    return len(text)
