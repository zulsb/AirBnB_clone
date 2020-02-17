#!/usr/bin/python3
"""
    Module define the FileStorage class.
"""
import json
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review


class FileStorage:
    """class FileStorage"""

    __file_path = "file.json"
    __objects = {}
    classes = {
            "BaseModel": BaseModel, "User": User,
            "Amenity": Amenity, "City": City, "State": State,
            "Place": Place, "Review": Review
            }

    def all(self):
        """Returns dictionary"""
        return self.__objects

    def new(self, obj):
        """Assigns objects"""
        self.__objects['{}.{}'.format(obj.__class__.__name__,
                                      obj.id)] = obj

    def save(self):
        """Writes an object to a file"""
        dic = {}
        for k, v in self.__objects.items():
            dic[k] = v.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(dic, f)

    def reload(self):
        """Retrieves objects from a file"""
        new = {}
        try:
            with open(self.__file_path, "r") as f:
                new = json.load(f)

                for k, v in new.items():
                    self.__objects[k] = self.classes[v["__class__"]](**v)
        except:
            pass
