#!/usr/bin/python3
"""
    Module for the Basemodel class
"""
import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """A base class for all instances"""
    def __init__(self, *args, **kwargs):
        """
            Initialize with public attributes(id, created_at, updated_at)
            *args: list of args
            **kwargs: key/value args
        """
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == 'created_at':
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """To print the string form of the object"""
        string = "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)
        return string

    def save(self):
        """updates the public instance attribute update_at with current time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary with key/value"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
