#!/usr/bin/python3
"""Module 5-to_json_string"""


import json


def to_json_string(my_obj):
    """Converts an string to a JSON object representation"""
    j_obj = json.dumps(my_obj)
    return j_obj
