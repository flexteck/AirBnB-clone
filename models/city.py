#!/usr/bin/python3
""" a class that define city and inherit from the BaseModel """

from models.base_model import BaseModel


class City(BaseModel):
    """ definition of public attributes """
    state_id = ""
    name = ""
