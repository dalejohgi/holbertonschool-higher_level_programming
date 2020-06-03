#!/usr/bin/python3
"""Module 2-read_lines"""


def read_lines(filename="", nb_lines=0):
    """Line counter for txt files"""

    line_counter = 0
    with open(filename, 'r', encoding='utf-8') as my_file:
        for lines in my_file:
            line_counter += 1
        my_file.seek(0)
        if nb_lines <= 0 or nb_lines >= line_counter:
            print(my_file.read(), end="")
        else:
            for i in range(nb_lines):
                print(my_file.readline(), end="")
