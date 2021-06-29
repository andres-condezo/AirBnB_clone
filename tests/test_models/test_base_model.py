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

    def test_attr_types(self):
        self.assertIs(type(self.obj.id), str)
        self.assertIs(type(self.obj.created_at), datetime)
        self.assertIs(type(self.obj.updated_at), datetime)

    def test_time_attrs(self):
        self.assertEqual(self.obj.created_at, self.obj.updated_at)
        self.assertLess(self.obj.created_at, self.obj2.created_at)

    def test__str__method(self):
        str_rep = "[{}] ({}) {}"\
                    .format(self.obj.__class__.__name__,
                            self.obj.id, self.obj.__dict__)
        self.assertEqual(self.obj.__str__(), str_rep)

    def test_to_dict_method(self):
        from_dict = self.obj.__dict__
        from_to_dict = self.obj.to_dict()

        self.assertIs(type(from_to_dict), dict)
        self.assertEqual(BaseModel.__name__, from_to_dict['__class__'])
        self.assertEqual(from_dict['id'], from_to_dict['id'])

    def test_to_dict_method_with_one_param(self):
        regex = 'takes 1 positional argument but 2 were given'
        with self.assertRaisesRegex(TypeError, regex):
            self.obj.to_dict(None)
        with self.assertRaisesRegex(TypeError, regex):
            self.obj.to_dict([])
        with self.assertRaisesRegex(TypeError, regex):
            self.obj.to_dict([1, 2, 3])
        with self.assertRaisesRegex(TypeError, regex):
            self.obj.to_dict({})
        with self.assertRaisesRegex(TypeError, regex):
            self.obj.to_dict({1, 2, 3})
        with self.assertRaisesRegex(TypeError, regex):
            self.obj.to_dict(True)
        with self.assertRaisesRegex(TypeError, regex):
            self.obj.to_dict(False)
        with self.assertRaisesRegex(TypeError, regex):
            self.obj.to_dict(dict())
        with self.assertRaisesRegex(TypeError, regex):
            self.obj.to_dict({'id': 123, 'created_at': datetime.now()})
        with self.assertRaisesRegex(TypeError, regex):
            self.obj.to_dict('Ranmod value')

    def test_save_method(self):
        objid = self.obj.id
        self.assertEqual(self.obj.id, objid)
        self.assertEqual(self.obj.created_at, self.obj.updated_at)

        self.obj.save()

        self.assertEqual(self.obj.id, objid)
        self.assertNotEqual(self.obj.created_at, self.obj.updated_at)
        self.assertLess(self.obj.created_at, self.obj.updated_at)

    def test_save_method_with_one_param(self):
        regex = 'takes 1 positional argument but 2 were given'
        with self.assertRaisesRegex(TypeError, regex):
            self.obj.save(None)
            self.obj.save([])
            self.obj.save([1, 2, 3])
            self.obj.save({})
            self.obj.save({1, 2, 3})
            self.obj.save(True)
            self.obj.save(False)
            self.obj.save(dict())
            self.obj.save({'id': 123, 'created_at': datetime.now()})
            self.obj.save('Ranmod value')

    def test_createBaseModel_from_dictionary_as_kwargs(self):
        id = str(uuid4())
        now = datetime.now().isoformat()
        my_dict = {
            'id': id,
            'name': 'Jhon Smith',
            'created_at': now,
            'updated_at': now
        }
        obj1 = BaseModel(**my_dict)

        self.assertEqual(obj1.id, id)
        self.assertEqual(obj1.name, 'Jhon Smith')
        self.assertEqual(now, obj1.created_at.isoformat())
        self.assertEqual(now, obj1.updated_at.isoformat())

    def test_createBaseModel_from_dictionary_as_kwargs_empty(self):
        empty_dict = dict()
        obj1 = BaseModel(**empty_dict)

        self.assertIs(type(obj1), BaseModel)
        self.assertIs(type(obj1.id), str)
        self.assertIs(type(obj1.created_at), datetime)
        self.assertIs(type(obj1.updated_at), datetime)

    def test_createBaseModel_from_dictionary_as_kwargs_diff_fileds(self):
        my_dict = {
            'name': 'Jhon Smith',
            'age': 34
        }

        obj = BaseModel(**my_dict)

        self.assertEqual(obj.name, 'Jhon Smith')
        self.assertEqual(obj.age, 34)

        regex = "object has no attribute 'id'"
        with self.assertRaisesRegex(AttributeError, regex):
            obj.id

        regex = "object has no attribute 'created_at'"
        with self.assertRaisesRegex(AttributeError, regex):
            obj.created_at

        regex = "object has no attribute 'updated_at'"
        with self.assertRaisesRegex(AttributeError, regex):
            obj.updated_at

    def test_createBaseModel_from_dictionary_as_kwargs_wrong_format(self):
        id = uuid4()
        now = datetime.now()
        my_dict = {
            'id': id,
            'name': 'Jhon Smith',
            'created_at': now,
            'updated_at': now
        }

        regex = 'must be str, not datetime.datetime'
        with self.assertRaisesRegex(TypeError, regex):
            BaseModel(**my_dict)

    def test_createBaseModel_from_args(self):
        args = [True, 'Random', 34.2]
        obj = BaseModel(*args)

        self.assertIs(type(obj.id), str)
        self.assertIs(type(obj.created_at), datetime)
        self.assertIs(type(obj.updated_at), datetime)

    def test_create_new_attrs(self):
        self.obj.name = 'Jhon'
        self.obj.age = 46

        self.assertEqual(self.obj.name, 'Jhon')
        self.assertEqual(self.obj.age, 46)


if __name__ == '__main__':
    unittest.main()
