#!/usr/bin/python3
"""Class MyList that inherits from list"""
class MyList(list):
    """
    A custom list class that inherits from the built-in list class.
    """
    def print_sorted(self):
        """
        Prints a list but sorted in ascending order
        """
        print(sorted(self))
