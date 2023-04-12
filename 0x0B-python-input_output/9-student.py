#!/usr/bin/python3
"""Define a student based on their first name,last and age"""


class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student with their first name, last name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the dictionary representation of a Student instance"""
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
        }
