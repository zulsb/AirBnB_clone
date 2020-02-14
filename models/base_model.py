#!/usr/bin/python3
"""
    Module define the BaseModel class and defines all
    common attributes/methods for other classes.
"""
import uuid
from datetime import datetime


class BaseModel:
    """ Class Base Model. """

    def __init__(self, *args, **kwargs):
        """ Initialize Base Model instance. """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, val in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    setattr(self, key, val)

    def __str__(self):
        """ Prints the BaseModel Attribute of String representation. """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ Save Method - Updates the attributes with current datetime. """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Method-Return a dictionary of keys/values of __dict__ """
        d = self.__dict__.copy()
        d["__class__"] = self.__class__.__name__
        d["updated_at"] = d["updated_at"].isoformat()
        d["created_at"] = d["created_at"].isoformat()
        return d
