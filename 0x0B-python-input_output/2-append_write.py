#!/usr/bin/python3

"""Append to a text file and return the number of characters added"""


def append_write(filename="", text=""):
    """Open file in append mode with UTF-8 encoding,
    write text to file, and return number of characters added"""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
