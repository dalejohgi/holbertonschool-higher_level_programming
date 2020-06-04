#!/usr/bin/python3
"""Moldule 6-from_json_string"""


import json


def from_json_string(my_str):
    """Converts json object into a Python object"""
    py_obj = json.loads(my_str)
    return py_obj
