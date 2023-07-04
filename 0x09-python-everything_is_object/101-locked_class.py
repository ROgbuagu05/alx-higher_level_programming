#!/usr/bin/python3
"""Defines a locked class"""

class LockedClass:
    """
    This class prevents user from dynamic attributes
    """
    __slots__ = ["first_name"]
