#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns a tuple with the length of a string and its first character."""
    length = len(sentence)
    first_char = sentence[0] if length else None
    tup = (length, first_char)
    return (tup)
