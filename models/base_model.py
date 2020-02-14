#!/usr/bin/python3
"""
    Module define the BaseModel class.
    defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """ class Base Model"""

    def __init__(self):
        """ initialize Base Model instance """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Prints the BaseModel Attribute of String representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ Save Method - Updates the attributes with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Dictionary Method-Return a dictionary of keys/values of __dict__"""
        d = self.__dict__.copy()
        d["__class__"] = self.__class__.__name__
        d["updated_at"] = d["updated_at"].isoformat()
        d["created_at"] = d["created_at"].isoformat()
        return d
