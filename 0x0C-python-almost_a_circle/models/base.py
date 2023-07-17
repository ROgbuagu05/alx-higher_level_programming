#!/usr/bin/python3
"""Module for base model class"""
import json
import csv
import os


class Base:
    """Base class for all other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor for Base.

        Parameters:
        id (int): The id value to assign to the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes JSON string representation of
        a list_objs to a file """
        filename = cls.__name__ + ".json"
        with open(filename, mode="w") as s_file:
            if list_objs is None:
                s_file.write("[]")
            else:
                s_file.write(cls.to_json_string(
                             [i.to_dictionary() for i in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """ returns list of JSON string
        representation """
        if json_string is None or len(json_string) == 0:
            return ("[]")
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns instance with all set attributes """
        if cls.__name__ == "Rectangle":
            temp_instance = cls(3, 3)
        elif cls.__name__ == "Square":
            temp_instance = cls(3)
        temp_instance.update(**dictionary)
        return temp_instance

    @classmethod
    def load_from_file(cls):
        """ returns list of instances """
        result = []
        filename = cls.__name__ + ".json"
        with open(filename, mode="r") as r_file:
            text = r_file.read()

        text = cls.from_json_string(text)
        for i in text:
            if type(i) == dict:
                result.append(cls.create(**i))
            else:
                result.append(item)
        return result

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serializes in CSV """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None:
                f.write("")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ deserializes in CSV """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dictionaries = csv.DictReader(csvfile,
                                                   fieldnames=fieldnames)
                list_dictionaries = [dict([i, int(j)]for i, j in dicti.items())
                                     for dicti in list_dictionaries]
                return [cls.create(**dicti) for dicti in list_dictionaries]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):

        # Create a turtle object
        turt = turtle.Turtle()
        turt.pensize(2)
        turt.shape("arrow")

        # Create a turtle object for drawing
        turt.color("navy")
        for rectangle in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rectangle.x, rectangle.y)
            turt.down()
            for i in range(2):
                turt.forward(rectangle.width)
                turt.left(90)
                turt.forward(rectangle.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("red")
        for square in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(square.x, square.y)
            turt.down()
            for i in range(4):
                turt.forward(square.width)
                turt.left(90)
            turt.hideturtle()

        turtle.done()
