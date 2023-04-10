#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        """
        Public instance method that prints the list sorted in ascending order.
        """
        sorted_list = sorted(self) # Sort the list in ascending order
        print(sorted_list) # Print the sorted list
