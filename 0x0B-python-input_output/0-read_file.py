#!/usr/bin/python3

"""this module is to read a text file."""

# Define a function to read a text file and print its contents to stdout


def read_file(filename=""):

    with open(filename, "r", encoding="utf-8") as file:

        contents = file.read()
        # Read file contents
        print(contents, end="")
        # Print file contents to stdout
