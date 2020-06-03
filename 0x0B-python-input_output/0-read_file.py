#!/usr/bin/python3
"""Module 0-read_file"""


def read_file(filename=""):
    """Read a txt file"""
    with open(filename, 'r', encoding='utf-8') as my_file:
        print(my_file.read())
