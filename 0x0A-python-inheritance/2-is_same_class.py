#!/usr/bin/python3
"""
Defines a function for is_same_class
"""
def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.

    Parameters:
    obj: The object to be checked
    a_class: The class to compare against

    Returns:
    bool: True if the object is exactly an instance of the specified class,
    False otherwise
    """
    return type(obj) == a_class
