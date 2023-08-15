#!/usr/bin/python3
"""importing JSON"""

import json

"""Define a class named Base"""


class Base(object):
    """this is a class named Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """This is a class constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """this is a method that returns
        the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """this is a method that writes
        the JSON string representation of list_objs to a file"""

        file_name = cls.__name__ + ".json"
        with open(file_name, 'w', encoding='utf-8') as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                list_dict = [object.to_dictionary() for object in list_objs]
                json_file.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """this is a method that returns
        the list of the JSON string representation"""

        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """this is a method that
        returns an instance with all attributes already set"""

        if cls.__name__ == "Square":
            dummy = cls(1)

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)

        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """this is a method that returns a list of instances"""

        file_name = cls.__name__ + ".json"

        try:
            with open(file_name, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]

        except IOError:
            return []
