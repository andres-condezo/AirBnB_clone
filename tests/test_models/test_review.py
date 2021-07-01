#!/usr/bin/python3
"""
    This module contains test cases for Review
"""
import unittest
from models.review import Review
import pep8
from models.base_model import BaseModel
from datetime import datetime


class TestReview(unittest.TestCase):
    """" Test cases class of Review """

    def test_pep8_review(self):
        """pep8 test.
        Makes sure the Python code is up to the pep8 standard.
        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/review.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_review(self):
        """ Test type of the attributes"""
        new_review = Review()
        self.assertIs(type(new_review.id), str)
        self.assertIs(type(new_review.created_at), datetime)
        self.assertIs(type(new_review.updated_at), datetime)
        self.assertIs(type(new_review.place_id), str)
        self.assertIs(type(new_review.user_id), str)
        self.assertIs(type(new_review.text), str)

    def test_inherit_Review(self):
        """ Test inherit """
        new_inherit = Review()
        self.assertIsInstance(new_inherit, BaseModel)

    def test_attr(self):
        """ Test if Review has attribute """
        new_review = Review()
        self.assertTrue(hasattr(new_review, "id"))
        self.assertTrue(hasattr(new_review, "created_at"))
        self.assertTrue(hasattr(new_review, "updated_at"))
        self.assertTrue(hasattr(new_review, "place_id"))
        self.assertTrue(hasattr(new_review, "user_id"))
        self.assertTrue(hasattr(new_review, "text"))

    def test_str_empty(self):
        """ Test if attribute is empty """
        new_review = Review()
        self.assertEqual(new_review.place_id, "")
        self.assertEqual(new_review.user_id, "")
        self.assertEqual(new_review.text, "")
