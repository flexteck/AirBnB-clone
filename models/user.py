#!/usr/bin/python3
from models.base_model import BaseModel

# A user class that inherit from BaseModel class

class User(BaseModel):
    """ initialization of instance """
    super().__init__
    self.email = ""
    self.password = ""
    self.first_name = ""
    self.last_name = ""
