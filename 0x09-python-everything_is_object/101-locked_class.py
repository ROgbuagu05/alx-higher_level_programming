#!/usr/bin/python3
"""Defines a LockedClass"""

class LockedClass:
    """
    This class prevents user from dynamic attributes
    """
    __slots__ = ["first_name"]
