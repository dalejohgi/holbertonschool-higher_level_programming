#!/usr/bin/python3
"""Module 13-student.py"""


class Student:
    """Class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializator for student class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dict representation of a student instance"""
        if attrs is None:
            return self.__dict__
        else:
            requested_attr = {}
            for atributes in attrs:
                try:
                    requested_attr[atributes] = self.__dict__[atributes]
                except KeyError:
                    pass
            return requested_attr

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for keys, values in json.items():
            setattr(self, keys, values)
