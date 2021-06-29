#!/usr/bin/python3
"""Base model class"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Defines all common attributes-methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes object"""
        if kwargs:
            for key, val in kwargs.items():
                if key != "__class__":
                    if key == "created_at":
                        val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                    if key == "updated_at":
                        val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, val)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns string representation"""
        return ("[{}] ({}) {}"
                .format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """Updates the public instance attr with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        dict_returned = dict(self.__dict__)
        dict_returned["__class__"] = self.__class__.__name__
        dict_returned["created_at"] = self.created_at.isoformat()
        dict_returned["updated_at"] = self.updated_at.isoformat()
        return dict_returned
