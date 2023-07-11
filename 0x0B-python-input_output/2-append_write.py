#!/usr/bin/python3
"""Appends a string to text file"""


def append_write(filename="", text=""):
    """
    A function that appends a string at the end of a text file (UTF8)

    Args:
    filename (str): The name of the file to append to.
    text (str): The string to be appended to the file.

    Returns:
    int: The number of characters added.
    """
    with open(filename, "a", encoding="utf8") as file:
        file.write(text)
        return len(text)
