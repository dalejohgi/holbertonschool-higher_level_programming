#!/usr/bin/python3
"""Module 9-add_item"""


from sys import argv
import json
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


filename = "add_item.json"
try:
    python_list = load_from_json_file(filename)
except FileNotFoundError:
    python_list = []

for argument in argv[1:]:
    python_list.append(argument)
save_to_json_file(python_list, filename)
