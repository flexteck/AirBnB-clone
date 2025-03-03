#!/usr/bin/python3
import uuid
from datetime import datetime
import models

class BaseModel:
    """ A class that defines all common attributes/methods for other classes """
    def __init__(self, *args, **kwargs):
        """ Initialize the baseModel instance """
        if kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ('created_at', 'updated_at'):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4()) 
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)


    def __str__(self):
        """ prints object details """
        return f"{[self.__class__.__name__]} {(self.id)} {self.__dict__}"

    def save(self):
        """ updates the public instance attribute 'updated_at' with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ return dictionary of all keys/values of the instance """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict

