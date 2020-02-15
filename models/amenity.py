#!/usr/bin/python3
"""
    Module define the Amenity class.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity class inherits from BaseModel.
        Public class attribute:
           name: string - empty string.
    """
    name = ""
