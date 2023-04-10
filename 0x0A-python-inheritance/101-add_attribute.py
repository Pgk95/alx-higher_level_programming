#!/usr/bin/env python3
"""
Module containing function that adds new attribute to object
"""


def add_attribute(obj, name, value):
    """
    Adds new attribute to object if possible
    """
    if not hasattr(obj, '__dict__'):
        # Raise TypeError if object doesn't have __dict__ attribute
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
