#!/usr/bin/python3

# Write a string to a text file and return the number of characters written
def write_file(filename="", text=""):
    # Open the file in write mode with UTF-8 encoding
    with open(filename, "w", encoding="utf-8") as file:
        # Write the text to the file and store the number of characters written
        count = file.write(text)
        # Return the number of characters written
        return count
