#!/usr/bin/python3
"""
Module for Square class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A square class that inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square. Defaults to 0.
            y (int, optional): The y-coordinate of the square. Defaults to 0.
            id (int, optional): The id of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns the string representation of the Square instance.

        Returns:
            str: The string representation of the Square instance.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Getter method for size.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for size.

        Args:
            value (int): The value to set the size to.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of a Square instance.

        Args:
            args: A tuple of the arguments to update.
            kwargs: A dictionary of the keyword arguments to update.
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.size = arg
                elif i == 1:
                    self.x = arg
                elif i == 2:
                    self.y = arg
                elif i == 3:
                    self.id = arg
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
                elif key == 'id':
                    self.id = value

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Square instance.

        Returns:
            dict: The dictionary representation of a Square instance.
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
