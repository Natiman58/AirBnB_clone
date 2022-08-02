#!/usr/bin/python3
"""
    The module containing the file storage class
"""
import json
import os

class FileStorage:
    """A class that serializes instances to a JSON file\
            and deserializes JSON file to instances:"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of the __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """saves in __objects; the obj with key as <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes(stringize) __objects to the JSON file (path: __file_path) """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            dict_string = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
            json.dump(dict_string, f)

    def reload(self):
        """ Deserialize(structurize) the json file """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            dict_struct = json.load(f) # stuck here
            dict_struct = {key: self.classes()[value["__class__"]]
                    (**value) for key, value in dict_struct.items()}
            FileStorage.__objects = dict_struct





