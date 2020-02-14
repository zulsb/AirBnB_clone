#!/usr/bin/python3
"""
    Module define the FileStorage class.
"""
import json


class FileStorage:
    """class FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Method to return dictionary """
        return self.__objects

    def new(self, obj):
        """Method to assign objects"""
        self.__objects['{}.{}'.format(obj.__class__.__name__,
                                      obj.id)] = obj.to_dict()

    def save(self):
        """Method write an object to a file - serialize"""
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f, default=str)

    def reload(self):
        """Method to retrieve objects from a file - Deserialize"""
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        except:
            pass
