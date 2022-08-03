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
        """Returns the dictionary; __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """saves in __objects; the obj with key as <obj class name>.id"""
        obj_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_name, obj.id)] = obj

    def save(self):
        """serializes(stringize) __objects to the JSON file (path: __file_path) """
        with open(FileStorage.__file_path, "w+", encoding="utf-8") as f:
            dict_string = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
            json.dump(dict_string, f)

    def reload(self):
        """Deserialize(structurize) the json file to __objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r+", encoding="utf-8") as f:
                dict_obj = json.load(f)

            





