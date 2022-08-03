#!/usr/bin/python3
"""
    A module for the class User
"""

from models.base_model import BaseModel


class User(BaseModel):
    """ class representing a User """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
