#!/usr/bin/python3
"""
This module contains a function that returns True if an object is an
instance of, or if the object is an instance of a class that inherited
from, the specified class. Otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Function that returns True if an object is an instance of, or if the
    object is an instance of a class that inherited from, the specified
    class. Otherwise False.
    Args:
        obj: the object to check
        a_class: the class to check against
    Returns:
        True if the object is an instance of, or if the object is an
        instance of a class that inherited from, the specified class.
        Otherwise False.
    """
    return isinstance(obj, a_class)
