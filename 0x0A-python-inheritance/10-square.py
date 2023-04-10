#!/usr/bin/python3
""" Module that defines a Square class """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class that inherits from Rectangle """

    def __init__(self, size):
        """ Initializes a new Square instance """

        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """ Returns a string representation of a Square """

        return "[Square] {}/{}".format(self.__size, self.__size)
