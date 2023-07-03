#!/usr/bin/python3
"""Defines a rectangle"""

class Rectangle:
    """
    This class defines a rectangle with width and height attributes.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle object with optional width and height.

        Parameters:
        width (int): The width of the rectangle. Defaults to 0
        height (int): The height of the rectangle. Defaults to 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
        int: The width of the rectangle
        """
        return (self._width)

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Parameters:
        value (int): The width value to be set

        Raises:
        TypeError: If width is not an integer
        ValueError: If width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.

        Returns:
        int: The height of the rectangle
        """
        return (self._height)

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Parameters:
        value (int): The height value to be set

        Raises:
        TypeError: If height is not an integer
        ValueError: If height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
