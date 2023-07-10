#!/usr/bin/python3
"""Module class for MyInt"""

class MyInt(int):
    """
    A class MyInt that inherits from int
    """

    def __eq__(self, other):
        """Overrides the == operator to return the inverted result."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Overrides the != operator to return the inverted result."""
        return super().__eq__(other)
