#!/usr/bin/python3
"""Adds all arguments to a Python list, and then saves them to a file"""

import sys
from os import path
from json import loads, dumps
from typing import List


def load_from_json_file(filename: str) -> List:
    """Loads JSON data from a file and returns the corresponding object"""
    with open(filename, mode='r', encoding='utf-8') as file:
        return loads(file.read())


def save_to_json_file(my_obj: List, filename: str) -> None:
    """Saves an object to a file in JSON format"""
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(dumps(my_obj))


if __name__ == "__main__":
    filename = "add_item.json"
    # check if file exists, if not create an empty list
    if path.isfile(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    # add arguments to the list
    for arg in sys.argv[1:]:
        my_list.append(arg)

    # save the updated list to the file
    save_to_json_file(my_list, filename)
