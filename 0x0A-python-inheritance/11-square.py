#!/usr/bin/python3
"""
This module defines a class Square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class defines a square
    """

    def __init__(self, size):
        """
        Initializes an instance of the Square class
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns the string representation of a Square object
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """
        Computes the area of a square
        """
        return self.__size ** 2
