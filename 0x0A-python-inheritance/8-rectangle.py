#!/usr/bin/python3
"""
Defines a class Rectangle that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
    """
    def __init__(self, width, height):
        """
        Initializes a new Rectangle.

        Parameters:
        width (int): The width of the rectangle
        height (int): The height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
