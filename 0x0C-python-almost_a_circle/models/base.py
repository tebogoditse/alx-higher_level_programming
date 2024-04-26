#!/usr/bin/python3
"""Base class"""
import json


class Base:

    """Define the class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        class_name = cls.__name__
        filename = f"{class_name}.json"
        text = []

        if list_objs is not None:
            for i in range(len(list_objs)):
                text.append(cls.to_dictionary(list_objs[i]))

        with open(filename, "w", encoding="UTF-8") as file:
            file.write(cls.to_json_string(text))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        name = cls.__name__
        filename = f"{name}.json"

        try:
            with open(filename, "r", encoding="UTF-8") as file:
                text_string = file.read()
            file = cls.from_json_string(text_string)
            li_instances = []
            for i in range(0, len(file)):
                li_instances.append(cls.create(**file[i]))
        except Exception as ex:
            li_instances = []

        return li_instances
