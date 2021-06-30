#!/usr/bin/python3
"""A module for the File Storage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.review import Review
from models.city import City
from models.state import State
from models.amenity import Amenity


class FileStorage:
    """File Storage Class"""

    __file_path = 'file.json'
    __objects = dict()

    def all(self):
        """All method: return the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = dict()
        for key, obj in FileStorage.__objects.items():
            new_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""

        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                new_dict = json.load(f)
                for dictionary in new_dict.values():
                    my_class = eval(dictionary["__class__"])
                    new_instance = my_class(**dictionary)
                    self.new(new_instance)
        except FileNotFoundError:
            pass
