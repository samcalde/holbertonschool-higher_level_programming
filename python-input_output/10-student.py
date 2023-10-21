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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        """
        if isinstance(attrs, list):
            if (all(isinstance(item, str) for item in attrs)):
                dictionary = vars(self)
                filtered_dic = {}
                for element in attrs:
                    if (element in dictionary):
                        filtered_dic[element] = dictionary[element]
                return filtered_dic

        return vars(self)
