#!/usr/bin/python3
"""
    Module define the City class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ City class inherits from BaseModel.
        Public class attributes:
            state_id:string will be State.id
            name:string - empty string
    """
    state_id = ""
    name = ""
