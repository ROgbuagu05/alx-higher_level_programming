#!/usr/bin/python3
"""Class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class representing a square, which inherits from Rectangle."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a square object.

        Parameters:
        size (int): The size of the square.
        x (int): The x-coordinate of the square's position.
        y (int): The y-coordinate of the square's position.
        id (int): The ID of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overloading the __str__ method."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """Getting size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """Setting size of square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updating square class"""
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returning dictionary representation of square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
