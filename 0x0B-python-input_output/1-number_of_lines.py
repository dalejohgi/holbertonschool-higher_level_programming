#!/usr/bin/python3
"""Module 1-number_of_lines"""


def number_of_lines(filename=""):
    """Line counter for txt files"""

    line_counter = 0
    with open(filename, encoding='utf-8') as my_file:
        for lines in my_file:
            line_counter += 1
    return line_counter
