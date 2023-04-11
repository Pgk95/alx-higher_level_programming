#!/usr/bin/python3

"""Write a string to a text file and return the number of characters written"""


def write_file(filename="", text=""):
    """
    Open file in write mode with UTF-8 encoding,
    write text to file,
    and return number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
