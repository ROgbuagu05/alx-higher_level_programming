#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific position in a list."""
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    
    for i in range(idx + 1, len(my_list)):
        my_list[i - 1] = my_list[i]

    my_list.pop()

    return (my_list)
