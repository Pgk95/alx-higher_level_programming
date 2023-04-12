#!/usr/bin/python3
"""
Module 11-student.py
"""


class Student:
    """Class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation method for the Student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method that retrieves a dictionary representation of a Student"""
        if attrs is not None and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """Method that replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
