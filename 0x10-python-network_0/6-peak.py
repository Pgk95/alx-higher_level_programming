#!/usr/bin/python3

"""finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    if not list_of_integers:
        return None


    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        current = list_of_integers[mid]
        next_num = list_of_integers[mid + 1]

        if current < next_num:
            low = mid + 1
        else:
            high = mid

    peak = list_of_integers[low]
    if low > 0 and peak < list_of_integers[low - 1]:
        return None

    return peak
