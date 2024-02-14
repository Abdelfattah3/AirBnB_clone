#!/usr/bin/python3
"""Filestorage that will handle the objects"""

import json
from models.base_model import BaseModel


class FileStorage:

    """Filestorage class for handling objects"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all the objects

        Returns:
            _type_: Dict
        """
        return self.__objects

    def new(self, obj):
        """sets new objects"""
        key_obj = str(obj.__class__.__name__) + "." + str(obj.id)
        value_obj = obj
        self.__objects[key_obj] = value_obj

    def save(self):
        """save the updated dictionary"""
        with open(self.__file_path, "w", encoding='UTF8') as file:
            json.dump(self.__objects, file)

    def reload(self):
        """reload from the json file"""
        with open(self.__file_path, "r", encoding='UTF8') as file:
            json.load(file)
