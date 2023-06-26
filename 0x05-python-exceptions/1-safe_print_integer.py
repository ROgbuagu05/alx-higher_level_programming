#!/usr/bin/python3
def safe_print_integer(value):
    """
    Prints an integer with "{:d}".format().

    Args:
        value: The value to print.

    Returns:
        True if value has been correctly printed
        Otherwise, returns False
    """
    try:
        print("{:d}".format(int(value)))
        return (True)
    except (TypeError, ValueError):
        return (False)
