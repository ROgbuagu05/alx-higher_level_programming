#!/usr/bin/python3
"""Module defining the Rectangle class"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Parameters:
        size (int): The size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculates the area of the square.

        Retrns:
        int: The area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """Returns the square description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
