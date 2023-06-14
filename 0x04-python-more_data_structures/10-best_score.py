#!/usr/bin/python3
"""Returns the key with the biggest integer value."""
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    best_score = max(a_dictionary.values(), key=a_dictionary.get)
    return (best_score)
