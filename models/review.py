#!/usr/bin/python3
"""
    A module for the Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
        A class for the review section
    """
    place_id = ""
    user_id = ""
    text = ""
