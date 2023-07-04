#!/usr/bin/python3
"""
Defines a function that prints a square with the character #.

Parameters:
    print_square: function that prints a square with the character #.
"""

def print_square(size):
    """
    This function prints a square with the character '#'.

    Parameters:
    size (int): The size length of the square

    Raises:
    TypeError: If size is not an integer and less than 0.
    ValueError: If size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
