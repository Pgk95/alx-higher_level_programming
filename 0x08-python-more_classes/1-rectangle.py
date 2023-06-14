#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    def __init__(self, width, height):

        self.width = width
        self.height = height

    def height(self):

        return 2 * (self.width + self.height)

    def width(self):

        return self.width * self.height
