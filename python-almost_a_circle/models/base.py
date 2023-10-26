#!/usr/bin/python3

"""
This module creates a class named Base
"""


import json

class Base:
    """
    Definition of the class
    """
    ___nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.increment_objects()
            self.id = Base.___nb_objects

    @classmethod
    def increment_objects(cls):
        cls.___nb_objects += 1
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Turns a dictionary into a JSON string representation
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return []
