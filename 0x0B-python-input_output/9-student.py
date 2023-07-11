#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """
    Defines a student.

    Attributes:
    first_name (str): The student's first name.
    last_name (str): The student's last name.
    age (int): The student's age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary representation of the Student instance.

        Returns:
        dict: The dictionary representation of the Student instance.
        """
        return self.__dict__
