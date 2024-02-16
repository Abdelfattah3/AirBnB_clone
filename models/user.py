#!/usr/bin/python3
"""User class for the user info"""

from base_model import BaseModel


class User(BaseModel):
    """User class for the user info"""

    def __init__(self):
        """initiate the class that inherit from basemodel"""
        super().__init__(self)
        self.email = ""
        self.password = ""
        self.first_nam = ""
        self.last_name = ""
