#!/usr/bin/python3
""" This module contains the Square class that inherits from Rectangle
    class from the module 9-rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A Square class that inherits from Rectangle class """
    def __init__(self, size):
        """ Constructor method that initializes the size of square """
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ Return the square description """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)

    def area(self):
        """ Return the area of the square """
        return self.__size * self.__size
