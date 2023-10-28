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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        if list_objs:
            objs_list = []
            for instance in list_objs:
                objs_list.append(instance.to_dictionary())
            with open(f'{cls.__name__}.json', 'w') as file:
                file.write(cls.to_json_string(objs_list))
        else:
            with open(f'{cls.__name__}.json', 'w') as file:
                json.dump([], file)

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Turns a dictionary into a JSON string
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string
        """
        if json_string:
            obj_list = json.loads(json_string)
            return obj_list
        return []

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set:
        """
        from rectangle import Rectangle
        from square import Square
        if cls == Square:
            instance = cls(1)
        else:
            instance = cls(1, 1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances based on a file
        """
        from rectangle import Rectangle
        from square import Square
        try:
            with open(f'{cls.__name__}.json', 'r') as file:
                data = file.read()
                dictionaries = cls.from_json_string(data)
            instances_list = []
            for dictionary in dictionaries:
                instance = cls.create(**dictionary)
                instances_list.append(instance)
            return instances_list
        except:
            return []
