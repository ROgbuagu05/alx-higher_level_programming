#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied by 2."""
    new_directory = a_dictionary.copy()
    list_keys = list(new_directory.keys())

    for i in list_keys:
        new_directory[i] *= 2

    return (new_directory)
