#!/usr/bin/python3
"""Basemodel class that will be inheeited"""
from datetime import datetime
from uuid import uuid4


class BaseModel:

    """Basemodel class that will be inheeited"""

    def __init__(self, *args, **kwargs):
        """inialization of the class attributes"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = str(datetime.isoformat())
                if key != '__class__':
                    setattr(self, key, value)

    def to_dict(self):
        """manipulating the dict of class to be human readable
        Returns:
            _type_: dict
        """
        ob_dict = self.__dict__.copy()
        ob_dict['__class__'] = str(self.__class__.__name__)
        ob_dict['created_at'] = self.created_at.isoformat()
        ob_dict['updated_at'] = self.updated_at.isoformat()
        return ob_dict

    def __str__(self):
        """Returns a string repersentation of the class
        Returns:
            _type_: string
        """
        dict_class = self.__dict__.copy()
        return f"[{self.__class__.__name__}] ({self.id}) {dict_class}"

    def save(self):
        """Update the time if the object is updated"""
        self.updated_at = datetime.now()
