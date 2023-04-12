#!/usr/bin/python3
"""
Module that contains the function load_from_json_file
"""

import json


def load_from_json_file(filename):
    """
    Creates an Object from a "JSON file"

    Args:
        filename (str): name of the file to read from

    Returns:
        object: Python data structure represented by the JSON string
    """

    with open(filename, 'r', encoding='utf-8') as f:
        json_string = f.read()
        obj = json.loads(json_string)
        return obj
