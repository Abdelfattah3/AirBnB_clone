#!/usr/bin/python3
"""Filestorage that will handle the objects"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:

    """Filestorage class for handling objects"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all the objects

        Returns:
            _type_: Dict
        """
        return FileStorage.__objects

    def new(self, obj):
        """sets new objects"""
        key_obj = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(key_obj, obj.id)] = obj

    def save(self):
        """save the updated dictionary"""
        dct = FileStorage.__objects
        obj_dict = {obj: dct[obj].to_dict() for obj in dct.keys()}
        with open(FileStorage.__file_path, "w", encoding='UTF8') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """reload from the json file"""
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as file:
                obj_dict = json.load(file)
            for o in obj_dict.values():
                class_name = o["__class__"]
                del o["__class__"]
                self.new(eval(class_name)(**o))
        except FileNotFoundError:
            return
