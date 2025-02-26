#!/usr/bin/python3
""" a class that define place and inherit from BaseModel """

from models.base_model import BaseModel


class Place(BaseModel):
    """ defining class attributes """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    latitude = 0.0
    longtitude = 0.0
    amenity_ids = [] #aminity.id
