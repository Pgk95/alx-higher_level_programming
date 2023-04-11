#!/usr/bin/python3

# Read a text file and print its contents to stdout
def read_file(filename=""):
    # Open the file in read mode with UTF-8 encoding
    with open(filename, "r", encoding="utf-8") as file:
        # Read the contents of the file into a string
        contents = file.read()
        # Print the contents to stdout
        print(contents, end="")
