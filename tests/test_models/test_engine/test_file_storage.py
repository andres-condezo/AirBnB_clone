#!/usr/bin/python3
""" This module contains test cases for FileStorage"""
import json
import os
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """" Test cases class for FileStorage """

    def setUp(self):
        """ Setup function for TestFileStorage """
        super().setUp()
        self.file_path = 'file.json'

    def test_instance_creation(self):
        """ Test for FfileStorage instance creation """
        my_storage = FileStorage()
        self.assertIs(type(my_storage), FileStorage)

    def test_method_all(self):
        """ Test method 'all' of storage """
        all = storage.all()
        empty_dict = dict()

        if os.path.exists(self.file_path):
            self.assertNotEqual(all, empty_dict)
        else:
            self.assertDictEqual(all, empty_dict)


if __name__ == '__main__':
    unittest.main()
