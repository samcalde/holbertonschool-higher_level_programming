#!/usr/bin/python3

"""
Definition of a class Square, that inherits from Rectangle
"""


from models.rectangle import Rectangle
class Square(Rectangle):
    """
    Definition of class and methods of Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Replaces the str method to print [Square] (<id>) <x>/<y> - <size>
        """
        line1 = f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y}"
        line2 = f" - {self.width}"
        return (line1 + line2)

    @property
    def size(self):
        """
        Returns size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        size setter
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates attributes of the Square
        """
        dictionary = {1: "id", 2: "size", 3: "x", 4: "y"}
        if args:
            i = 1
            for argument in args:
                self.integer_validator(dictionary[i], argument)
                setattr(self, dictionary[i], argument)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
    
    def to_dictionary(self):
        """
        Returns dict representation of instance
        """
        dict1 = {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
        return dict1
