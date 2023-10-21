#!/usr/bin/python3

"""
Creates the class 'Student'
"""


class Student():
    """
    'Student' class
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiation of the class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance
        """
        return vars(self)
