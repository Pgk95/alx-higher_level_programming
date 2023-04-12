#!/usr/bin/python3

"""Return the JSON representation of an object (string)"""

import json


def to_json_string(my_obj):
    """Return the JSON representation of an object using json.dumps"""
    return json.dumps(my_obj)
