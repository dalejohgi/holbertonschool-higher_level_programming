#!/usr/bin/python3
"""Module 11-student.py"""


class Student:
    """Class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializator for student class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dict representation of a student instance"""

        return self.__dict__
