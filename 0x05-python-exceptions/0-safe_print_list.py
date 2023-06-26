#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list.

    Args:
        my_list: The list to print.
        x: The number of elements to print.

    Returns:
        The real number of elements printed.
    """
    counter = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            counter += 1
        except IndexError:
            break
    print("")
    return (counter)
