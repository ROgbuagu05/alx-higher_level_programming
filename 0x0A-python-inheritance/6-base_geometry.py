#!/usr/bin/python3
"""
Defines a class BaseGeometry based on 5-base_geometry.py
"""
class BaseGeometry:
    """
    A class representing a base geometry.

    Methods:
    area(): Raises an Exception with the message
    "area() is not implemented"
    """

    def area(self):
        """
        This method raises an Exception indicating that the
        area() method is not implemented.

        Raises:
        Exception: Indicates that the area() method is not implemented.
        """
        raise Exception("area() is not implemented")
