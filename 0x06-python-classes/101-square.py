#!/usr/bin/python3
"""Define a class Square."""

class Square:
    """
    This class defines a square by its size and position.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Parameters:
        size (int): The size of the square
        position (tuple): The position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
        int: The size of the square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Parameters:
        value (int): The new size of the square

        Raises:
        TypeError: If value is not an integer
        ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Gets the position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Parameters:
        value (tuple): The new position of the square

        Raises:
        TypeError: If value is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if i < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square."""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square with # to stdout"""
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ",  end="")
                print("#" * (self.__size))

    def __str__(self):
        """
        Prints square offsetting it by position with symbol #

        Returns:
        Square
        """
        if self.__size == 0:
            return("")
        new_lines = '\n' * self.position[1]
        spaces = ' ' * self.position[0]
        hashes = '#' * self.size
        return (new_lines + '\n'.join(spaces + hashes for e in range(self.size)))
