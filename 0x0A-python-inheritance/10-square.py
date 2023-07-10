#!/usr/bin/python3
"""
A class Square that inherits from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Initialize the square"""
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)

    def area(self):
        """Calculates the area"""
        return self.__size ** 2
