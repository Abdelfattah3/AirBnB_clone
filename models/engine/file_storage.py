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
        dct = {}
        for key, value in FileStorage.__objects.items():
            dct[key] = value.to_dict()
        with open(self.__file_path, "w", encoding='UTF8') as file:
            json.dump(dct, file)

    def reload(self):
        """reload from the json file"""
        try:
            with open(self.__file_path, "r", encoding='UTF8') as file:
                FileStorage.__objects = json.load(file)
            for key, value in FileStorage.__objects.items():
                class_name = value["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**value)
        except FileNotFoundError:
            pass
