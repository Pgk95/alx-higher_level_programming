#!/usr/bin/python3
# 0-add_integer.py
"""Defines an integer addition function."""

def add_integer(a, b=98):
    """Return the integer addition of a and b.
    float arguments are tyoecasted to ints before addition is performed.
    Raises:
        TypeError: If either of a and b is a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
