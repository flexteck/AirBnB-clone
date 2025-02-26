#!/usr/bin/python3
""" a class that define city and inherit from the BaseModel """

from models.basemodel import BaseModel


class City(BaseModel):
    """ definition of public attributes """
    state_id = ""
    name = ""
