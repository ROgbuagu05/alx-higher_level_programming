#!/usr/bin/python3
"""Defines a rectangle"""

class Rectangle:
    """
    Class that defines properties of rectangle by: (based on 2-rectangle.py).

    Parameters:
    width (int): width of the rectangle.
    height (int): height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle object with optional width and height.

        Parameters:
        width (int): The width of the rectangle (default is 0)
        height (int): The height of the rectangle (default is 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for the width attribute.

        Returns:
        int: The width of the rectangle
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Parameters:
        value (int): The width value to be set

        Raises:
        TypeError: If the width value is not an integer
        ValueError: If the width value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.

        Returns:
        int: The height of the rectangle
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Parameters:
        value (int): The height value to be set

        Raises:
        TypeError: If the height value is not an integer
        ValueError: If the height value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
        int: The area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
        int: The perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
        str: The string representation of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return ""

        rectangle_str = ""
        for y in range(self.height):
            rectangle_str += "#" * self.width + "\n"
        return rectangle_str
