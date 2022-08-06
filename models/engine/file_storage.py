#!/usr/bin/python3
"""
    The module containing the file storage class
"""
import json
import os
import datetime


class FileStorage:
    """A class that serializes instances to a JSON file\
            and deserializes JSON file to instances:"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all the dictionaries in __objects"""
        all_dicts = FileStorage.__objects
        return all_dicts

    def new(self, obj):
        """adds a new obj with key (<obj class name>.id) to __objects"""
        obj_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_name, obj.id)] = obj

    def save(self):
        """serializes(stringize) __objects\
                to the JSON file; __file_path"""
        J_file = FileStorage.__file_path
        the_dict = FileStorage.__objects
        with open(J_file, "w+", encoding="utf-8") as f:
            dict_K_V = {key: value.to_dict()
                        for key, value in the_dict.items()}
            json.dump(dict_K_V, f)

    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """Deserialize(structurize) the json file to __objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r+", encoding="utf-8") as f:
            dict_obj = json.load(f)
            dict_obj = {key: self.classes()[val["__class__"]](**val)
                        for key, val in dict_obj.items()}
            FileStorage.__objects = dict_obj

    def attributes(self):
        """Returns the valid attributes and their types for classname."""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
