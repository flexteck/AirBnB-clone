#!/usr/bin/python3
""" This module defines a class to manage storage for AirBnB clone """

import json
from models.base_model import BaseModel


class FileStorage:
    """  A class that serialiazes instancess to a JSON file and deserializes JSON file to instances """

    def __init__(self):
        self.__file_path ='file.json'
        self.__objects = {}


    def all(self):
        """ returns the dictionary of a stored objects """
        return self.__objects

    def new(self, obj):
        """ add a new objects to __objecct with key <class name>.id """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj


    def save(self):
        """ serializes __object to JSON file"""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}

        with open(self.__file_path, "w") as file:
            json.dump(obj_dict, file)


    def reload(self):
        """ deserializes the json file to object if the file exist """
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, obj_data in obj_dict.items():
                    class_name = obj_data["__class__"]
                    self.__objects[key] = eval(class_name)(**obj_data)
        except FileNotFoundError:
            pass
