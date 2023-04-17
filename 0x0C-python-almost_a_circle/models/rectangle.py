#!/usr/bin/python3

"""This module defines the Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """This class defines a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a rectangle instance"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def width(self):
        """Getter for the width attribute"""

        return self.__width

    def width(self, value):
        """Setter for the width attribute"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    def height(self):
        """Getter for the height attribute"""

        return self.__height

    def height(self, value):
        """Setter for the height attribute"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    def x(self):
        """Getter for the x attribute"""
        return self.__x

    def x(self, value):
        """Setter for the x attribute"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    def y(self):
        """Getter for the y attribute"""
        return self.__y

    def y(self, value):
        """Setter for the y attribute"""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Computes the area of the rectangle instance"""

        return self.width * self.height

    def display(self):
        """Prints the rectangle instance in stdout"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Returns the string representation of the rectangle instance"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **Kwargs):
        """Assigns an argument to each attribute of the Rectangle instance"""

        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]
        if len(args) == 0 or args is None:
            for key, value in Kwargs.items():
                setattr(self, key, value)
