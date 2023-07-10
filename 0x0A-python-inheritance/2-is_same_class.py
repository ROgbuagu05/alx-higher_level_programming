#!/usr/bin/python3
"""
Defines a function for is_same_class
"""
def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.

    Returns:
    If the object is exactly an instance of the specified class - True
    Otherwise - False
    """
    return (type(obj) is a_class)
