#!/usr/bin/python3
"""Review class for the Review info"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class for the Review info"""

    place_id = ""
    user_id = ""
    text = ""
