#!/usr/bin/python3
"""Deletes a key in a dictionary."""
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary is not None:
        a_dictionary.pop(key)
    return (a_dictionary)
