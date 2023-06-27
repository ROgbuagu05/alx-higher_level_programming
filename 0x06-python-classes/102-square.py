#!/usr/bin/python3
class Square:
    """
    This class defines a square by its size.
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
        size (int): The size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """
        Gets the size of the square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Parameters:
        value (int): The size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
        int: The area of the square.
        """
        return (self.__size * self.__size)

    def __eq__(self, other):
        """
        Checks if two squares are equal.

        Parameters:
        other (Square): The other square to compare to.

        Returns:
        bool: True if the squares are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Checks if two squares are not equal.

        Parameters:
        other (Square): The other square to compare to.

        Returns:
        bool: True if the squares are not equal, False otherwise.
        """
        return (self.area() != other.area())

    def __gt__(self, other):
         """
        Checks if one square is greater than the other.

        Parameters:
        other (Square): The other square to compare to.

        Returns:
        bool:
        return (self.area() > other.area())
        """

    def __ge__(self, other):
        """
        Define the >= compmarison to a Square.
        """
        return (self.area() >= other.area())

    def __lt__(self, other):
        return (self.area() < other.area())

    def __le__(self, other):
        return (self.area() <= other.area())
