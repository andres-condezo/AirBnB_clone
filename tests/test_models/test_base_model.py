#!/usr/bin/env python3
"""
    This module contains test cases for base_case.py
"""
import unittest
from uuid import uuid4
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """" Test cases class """
    def setUp(self) -> None:
        super().setUp()
        self.obj = BaseModel()
        self.obj2 = BaseModel()

    def test_pep8_base_model(self):
        """pep8 test.
        Makes sure the Python code is up to the pep8 standard.
        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/base_model.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_attr_types(self):
        self.assertIs(type(self.obj.id), str)
        self.assertIs(type(self.obj.created_at), datetime)
        self.assertIs(type(self.obj.updated_at), datetime)

if __name__ == '__main__':
    unittest.main()        
