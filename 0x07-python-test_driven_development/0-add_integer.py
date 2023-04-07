#!/usr/bin/python3
# 0-add_integer.py
"""Defines an integer addition of a and b"""


def add_integer(a, b=98):
    """
    Return the integer addition of int a and int b.
    TypeError: if either of them a or b is a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
