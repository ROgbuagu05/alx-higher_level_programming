#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    """
    Prints an integer.

    Args:
        value: The value to be printed.

    Returns:
        True if value has been correctly printed (it means the value is an integer),
        False otherwise.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return (False)
    else:
        return (True)
