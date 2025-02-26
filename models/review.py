#!/usr/bin/python3
""" a Review class that inherits from BaseModel """

from models.base_model import BaseModel


class Review(BaseModel):
    """ definition of class attributes """
    place_id = ""
    user_id = ""
    text = ""
