#!/usr/bin/python
"""
Module containing a Base class.
"""


class Base:
    """
    A base class with a private class attribute `__nb_objects` set to 0.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of Base.

        Args:
            id (int): an integer to assign to the instance's id attribute.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
