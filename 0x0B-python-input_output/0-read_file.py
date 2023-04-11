#!/usr/bin/python3

"""Read a text file and print its contents to stdout"""


def read_file(filename=""):
    """
    Open the file in read mode with UTF-8 encoding,
    read the contents of the file into a string,
    and print the contents to stdout.
    """
    with open(filename, "r", encoding="utf-8") as file:
        contents = file.read()
        print(contents, end="")
