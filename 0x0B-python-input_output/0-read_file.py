#!/usr/bin/python

# Define a function to read a text file and print its contents to stdout


def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as file:

        contents = file.read()

        # Read file contents

        print(contents)

        # Print file contents to stdout
