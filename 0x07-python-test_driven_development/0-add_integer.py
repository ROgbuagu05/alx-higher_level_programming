#!/usr/bin/python3
"""
Defines an integer addition function.
"""
def add_integer(a, b=98):
    """
    Function that adds two integer and/or float numbers

    Parameters:
    a: The first number to be added
    b: The second number to be added (default value is 98)

    Returns:
    int: The sum of a and b

    Raises:
    TypeError: If a or b aren't integer and/or float numbers
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
