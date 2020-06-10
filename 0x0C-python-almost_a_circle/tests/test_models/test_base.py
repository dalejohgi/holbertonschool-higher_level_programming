#!/usr/bin/python3
"""Test module for base"""


import unittest
import pycodestyle
import json
from models import base
Base = base.Base


class TestHbRequirements(unittest.TestCase):
    """Tests for Holberton Requirements"""

    @classmethod
    def setUpClass(cls):
        """Print an init message"""
        print("\n\n\nThis is the new Checker of Holberton School, "
              "now checking the \"base module\" :)\n\nChecking...\n\n")

    def test_conformance(self):
        """Check for pycodestyle - PEP8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['./models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_mod_doc(self):
        """Checks the module documentation"""
        self.assertGreater(len(base.__doc__), 0)

    def test_cls_doc(self):
        """Checks the class documentation"""
        self.assertGreater(len(Base.__doc__), 0)


class TestFunctionalities(unittest.TestCase):
    """Testing functions"""

    @classmethod
    def setUpClass(cls):
        """Set up some objects """

    def test_id(self):
        """Tests for the id generator"""
        b1 = Base()
        b2 = Base()
        b3 = Base(508)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 508)
        self.assertEqual(b4.id, 3)

    def test_a_lot_of_args(self):
        """Test for many arguments passed to Base"""
        with self.assertRaises(TypeError):
            b1 = Base(1, 2, 3, 4)

    def test_to_json_string(self):
        """Test the output of in the correct format(str)"""
        dic1 = {'x': 2, 'y': 8}
        dict2 = {'x': 4, 'y': 16}
        list_a = [dic1, dict2]
        self.assertTrue(type(Base.to_json_string(list_a)) is str)
        self.assertTrue(Base.to_json_string(list_a) == json.dumps(list_a))

    def test_none_to_json_string(self):
        """Test for an empty/None list of dicts"""
        list_a = []
        self.assertEqual(Base.to_json_string(list_a), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_from_json_string(self):
        """Test the output of in the correct format(py-obj)"""
        dic1 = {'x': 2, 'y': 8}
        dict2 = {'x': 4, 'y': 16}
        list_a = [dic1, dict2]
        str_rp = json.dumps(list_a)
        empty = []
        self.assertTrue(type(Base.from_json_string(str_rp)) is list)
        self.assertEqual(Base.from_json_string(str_rp), list_a)
        self.assertEqual(Base.from_json_string(None), empty)
