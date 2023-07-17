#!/usr/bin/python3
"""Class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """A class representing a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor for Rectangle.

        Parameters:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle. Defaults to 0.
        y (int): The y-coordinate of the rectangle. Defaults to 0.
        id (int): The id value to assign to the instance.
        
        Raises:
        TypeError: If either of width or height is not an int.
        ValueError: If either of width or height <= 0.
        TypeError: If either of x or y is not an int.
        ValueError: If either of x or y < 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """The width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting the width of the rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """The height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting the height of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """The x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setting the x coordinate of the rectangle"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """The y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setting the y coordinate of the rectangle"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """The area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Printing the rectangle in stdout"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Update the class Rectangle by overriding the __str__ method"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Updating the rectangle"""
        if args:
            for i in range(len(args)):
                if i == 0:
                    if type(args[i]) is not int:
                        raise TypeError("id must be an integer")
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) is not int:
                        raise TypeError("id must be an integer")
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returning the dictionary representation of the rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
