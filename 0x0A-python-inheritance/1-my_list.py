#!/usr/bin/python3
"""
Module containing MyList class that inherits from list
"""


class MyList(list):
    """
    MyList class that inherits from list
    """
    def print_sorted(self):
        """
        Public instance method that prints the list in ascending order
        """
        print(sorted(self))
