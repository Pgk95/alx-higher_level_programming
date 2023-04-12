#!/usr/bin/python3
"""Returns the dictionary description with simple data structure."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization
    of an object.

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary containing the serializable attributes of the obj.
    """
    return obj.__dict__
