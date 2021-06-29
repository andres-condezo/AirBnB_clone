#!/usr/bin/python3
"""
    This module contains test cases for FileStorage
"""
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

    def test_method_all_with_one_param(self):
        """ Tests for method 'all' with one param """

        regex = 'takes 1 positional argument but 2 were given'
        with self.assertRaisesRegex(TypeError, regex):
            storage.all(None)
        with self.assertRaisesRegex(TypeError, regex):
            storage.all([])
        with self.assertRaisesRegex(TypeError, regex):
            storage.all([1, 2, 3])
        with self.assertRaisesRegex(TypeError, regex):
            storage.all({})
        with self.assertRaisesRegex(TypeError, regex):
            storage.all({1, 2, 3})
        with self.assertRaisesRegex(TypeError, regex):
            storage.all(True)
        with self.assertRaisesRegex(TypeError, regex):
            storage.all(False)
        with self.assertRaisesRegex(TypeError, regex):
            storage.all(dict())
        with self.assertRaisesRegex(TypeError, regex):
            storage.all({'id': 123})
        with self.assertRaisesRegex(TypeError, regex):
            storage.all('Ranmod value')

    def test_method_new(self):
        """ Test that 'new' method stores an object correctly """
        obj = BaseModel()
        key = "{}.{}".format(type(obj).__name__, obj.id)

        all_objs = storage.all()
        storage.new(obj)

        self.assertEqual(obj, all_objs[key])

    def test_method_new_with_one_param(self):
        """ Tests for method 'new' with one param different than expected """

        regex = "object has no attribute 'id'"
        with self.assertRaisesRegex(AttributeError, regex):
            storage.new(None)
        with self.assertRaisesRegex(AttributeError, regex):
            storage.new([])
        with self.assertRaisesRegex(AttributeError, regex):
            storage.new([1, 2, 3])
        with self.assertRaisesRegex(AttributeError, regex):
            storage.new({})
        with self.assertRaisesRegex(AttributeError, regex):
            storage.new({1, 2, 3})
        with self.assertRaisesRegex(AttributeError, regex):
            storage.new(True)
        with self.assertRaisesRegex(AttributeError, regex):
            storage.new(False)
        with self.assertRaisesRegex(AttributeError, regex):
            storage.new(dict())
        with self.assertRaisesRegex(AttributeError, regex):
            storage.new({'id': 123})
        with self.assertRaisesRegex(AttributeError, regex):
            storage.new('Ranmod value')

    def test_method_new_with_two_params(self):
        """ Test 'new' method with two positional args """
        obj = BaseModel()

        regex = 'takes 2 positional arguments but 3 were given'
        with self.assertRaisesRegex(TypeError, regex):
            storage.new(obj, None)
        with self.assertRaisesRegex(TypeError, regex):
            storage.new(obj, [])
        with self.assertRaisesRegex(TypeError, regex):
            storage.new(obj, [1, 2, 3])
        with self.assertRaisesRegex(TypeError, regex):
            storage.new(obj, {})
        with self.assertRaisesRegex(TypeError, regex):
            storage.new(obj, {1, 2, 3})
        with self.assertRaisesRegex(TypeError, regex):
            storage.new(obj, True)
        with self.assertRaisesRegex(TypeError, regex):
            storage.new(obj, False)
        with self.assertRaisesRegex(TypeError, regex):
            storage.new(obj, dict())
        with self.assertRaisesRegex(TypeError, regex):
            storage.new(obj, {'id': 123})
        with self.assertRaisesRegex(TypeError, regex):
            storage.new(obj, 'Ranmod value')

    def test_save_method(self):
        """ Tests for 'save' method """
        prev_all_objs = storage.all()

        obj = BaseModel()
        key = "{}.{}".format(type(obj).__name__, obj.id)

        self.assertIn(key, prev_all_objs.keys())

        with open('file.json', mode='r', encoding='utf-8') as file:
            dict_loaded = json.load(file)

            self.assertIs(type(dict_loaded), dict)
            self.assertNotIn(key, dict_loaded.keys())

        storage.save()

        with open('file.json', mode='r', encoding='utf-8') as file:
            dict_loaded = json.load(file)

            self.assertIs(type(dict_loaded), dict)
            self.assertIn(key, dict_loaded.keys())

    def test_save_method_with_one_param(self):
        """ Test for 'save' method with one param """
        regex = 'takes 1 positional argument but 2 were given'
        with self.assertRaisesRegex(TypeError, regex):
            storage.save(None)
        with self.assertRaisesRegex(TypeError, regex):
            storage.save([])
        with self.assertRaisesRegex(TypeError, regex):
            storage.save([1, 2, 3])
        with self.assertRaisesRegex(TypeError, regex):
            storage.save({})
        with self.assertRaisesRegex(TypeError, regex):
            storage.save({1, 2, 3})
        with self.assertRaisesRegex(TypeError, regex):
            storage.save(True)
        with self.assertRaisesRegex(TypeError, regex):
            storage.save(False)
        with self.assertRaisesRegex(TypeError, regex):
            storage.save(dict())
        with self.assertRaisesRegex(TypeError, regex):
            storage.save({'id': 123})
        with self.assertRaisesRegex(TypeError, regex):
            storage.save('Ranmod value')

    def test_reload_method(self):
        """ Test cases for 'reload' method """
        prev_dict = storage.all()

        storage.reload()

        self.assertDictEqual(prev_dict, storage.all())

    def test_reload_method_with_one_param(self):
        """ Tests for reload method passing one param """
        with self.assertRaises(TypeError):
            storage.reload(None)
        with self.assertRaises(TypeError):
            storage.reload([])
        with self.assertRaises(TypeError):
            storage.reload([1, 2, 3])
        with self.assertRaises(TypeError):
            storage.reload({})
        with self.assertRaises(TypeError):
            storage.reload({1, 2, 3})
        with self.assertRaises(TypeError):
            storage.reload(True)
        with self.assertRaises(TypeError):
            storage.reload(False)
        with self.assertRaises(TypeError):
            storage.reload(dict())
        with self.assertRaises(TypeError):
            storage.reload({'id': 123})
        with self.assertRaises(TypeError):
            storage.reload('Ranmod value')


if __name__ == '__main__':
    unittest.main()
