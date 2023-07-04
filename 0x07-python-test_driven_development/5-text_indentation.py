#!/usr/bin/python3
"""
Defines a function that prints a text with 2 new lines after each,
of these characters: . ? and :
Attributes:
    text_indentation: function that prints a text with specific conditions
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after ., ?, : characters.

    Parameters:
    text (str): The text to be indented

    Raises:
    TypeError: If the input text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")
