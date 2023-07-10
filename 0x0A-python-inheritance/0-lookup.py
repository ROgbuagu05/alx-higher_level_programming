#!/usr/bin/python3
def lookup(obj):
  """Returns a list of available attributes and methods of an object."""
  attributes = []
  for key in dir(obj):
    if not key.startswith("_"):
      attributes.append(key)
  return attributes
