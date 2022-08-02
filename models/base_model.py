#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """A base class for all instances"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """To print the string form of the object"""
        string = "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)
        return string

    def save(self):
        """updates the public instance attribute update_at with current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary with key/value"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
