#!/usr/bin/python3

# This function reads a text file (UTF-8) and prints its contents to stdout.
# It uses the 'with' statement to ensure proper file handling and doesn't handle
# any file permission or file not found exceptions.
def read_file(filename=""):
    # Open the file in read mode with UTF-8 encoding
    with open(filename, "r", encoding="utf-8") as file:
        # Read the contents of the file into a string
        contents = file.read()
        # Print the contents to stdout without adding a newline at the end
        print(contents, end="")
