#!/usr/bin/python3
"""Defines based on 9-student.py"""


class Student:
    """A class representing a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the object"""
        if attrs is None:
            return self.__dict__
        else:
            obj_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    obj_dict[attr] = getattr(self, attr)
            return obj_dict

    def reload_from_json(self, json):
        """Replace attributes of the object with values from a JSON string"""
        for key, value in json.items():
            setattr(self, key, value)
