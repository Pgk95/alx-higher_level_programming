#!/usr/bin/python3
"""Empty class BaseGeometry"""


class BaseGeometry:
    """Empty class BaseGeometry"""
    def area(self):
        """Method to raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to validate value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
