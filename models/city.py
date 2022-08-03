#!/usr/bin/python3

"""A module containing the city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class representing a City."""
    state_id = ""
    name = ""
