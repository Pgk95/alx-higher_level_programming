#!/usr/bin/python3
"""This module defines a class Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class"""

    def __init__(self, width, height):
        """Instantiation method"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Method that returns the area of the rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """String representation of the object"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
