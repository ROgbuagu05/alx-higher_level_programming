#!/usr/bin/python3
"""Module for base of all bases"""
import os


class Base:
    """Base class for all other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor for Base.

        Parameters:
        id (int): The id value to assign to the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
