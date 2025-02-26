#!/usr/bin/python3
""" class that define amenities and inherits from BaseModel"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ define class attributes """
    name = ""
