#!/usr/bin/python3
def new_in_list(my_list, idx, element):
  """Replaces an element of a list at a specific position."""
  tmp_list = my_list[:]

  if 0 <= idx < len(my_list):
      tmp_list[idx] = element
    return tmp_list
