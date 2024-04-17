#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """Write a class Student that defines a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for key, value in self.__dict__.items():
            for i in attrs:
                if key == i:
                    new_dict[key] = value

        return new_dict
