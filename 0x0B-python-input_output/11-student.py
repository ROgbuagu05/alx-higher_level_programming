#!/usr/bin/python3
"""Defines a class student"""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Parameters:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Parameters:
        attrs (list): A list of attribute names to be retrieved (optional)

        Returns:
        dict: A dictionary representation of the Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr
                    in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance

        Parameters:
        json (dict): A dictionary containing the attributes to be set.
        """
        for attr, value in json.items():
            setattr(self, attr, value)
