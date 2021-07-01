#!/usr/bin/python3
"""
    This module contains test cases for Amenity
"""
import unittest
from models.amenity import Amenity
import pep8
from models.base_model import BaseModel
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """" Test cases class of Amenity """

    def test_pep8_amenity(self):
        """pep8 test.
        Makes sure the Python code is up to the pep8 standard.
        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/amenity.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_attr(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))
        self.assertTrue(hasattr(amenity, "name"))

    def test_type(self):
        amenity = Amenity()
        self.assertEqual(type(amenity.id), str)
        self.assertEqual(type(amenity.created_at), datetime)
        self.assertEqual(type(amenity.updated_at), datetime)
        self.assertEqual(type(amenity.name), str)

    def test_attrIsempty(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
