#!/usr/bin/python3
"""Defines a function for a lookup"""
def lookup(obj):
    """
    Returns:
    The list of available attributes and methods of an object
    """
    return (dir(obj))