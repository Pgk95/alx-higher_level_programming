#!/usr/bin/python3

<<<<<<< HEAD
# Read a text file and print its contents to stdout
=======
"""This function reads a text file (UTF-8) and prints its contents to stdout"""

>>>>>>> 28c6f5bd6627855bf3118d05dd2c42509cad4e40
def read_file(filename=""):
    # Open the file in read mode with UTF-8 encoding
    with open(filename, "r", encoding="utf-8") as file:
        # Read the contents of the file into a string
        contents = file.read()
        # Print the contents to stdout
        print(contents, end="")
