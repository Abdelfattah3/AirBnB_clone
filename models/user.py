#!/usr/bin/python3
"""User class for the user info"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class for the user info"""

    email = ""
    password = ""
    first_nam = ""
    last_name = ""
