#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """ A class that defines all common attributes/methods for other classes """
    def __init__(self):
        """ Initialize the baseModel instance """
        self.id = str(uuid.uuid4()) 
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    def __str__(self):
        """ prints object details """
        return f"{[self.__class__.__name__]} {(self.id)} {self.__dict__}"

    def save(self):
        """ updates the public instance attribute 'updated_at' with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ return dictionary of all keys/values of the instance """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict

