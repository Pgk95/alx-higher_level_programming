#!/usr/bin/python3
"""Module defining MyInt class"""


class MyInt(int):
    """MyInt class inheriting from int"""

    def __eq__(self, other):
        """Invert the == operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert the != operator"""
        return super().__eq__(other)
