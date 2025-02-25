#!/usr/bin/python3
from models.base_model import BaseModel

# A user class that inherit from BaseModel class

class User(BaseModel):
    """creation of public instance"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    """ initialization of instance """
    super().__init__
