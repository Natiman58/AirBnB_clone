#!/usr/bin/env python3
"""
    A module that defines the base class for other classes
"""


class BaseModel:
    """
        The base class with public instance attributes:
            id:
            created_at: datetime - assign with the current datetime\
                when an instance is created
            updated_at: datetime - assign with the current datetime\
                when an instance is created\
                and it will be updated every time you change your object
    """
    
