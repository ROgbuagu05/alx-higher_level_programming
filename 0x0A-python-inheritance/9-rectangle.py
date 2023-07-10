#!/usr/bin/python3
"""
Defines a class Rectangle based on 8-base_geometry.py.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle object with the given width and height.

        Paameters:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
        int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
        str: The string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
