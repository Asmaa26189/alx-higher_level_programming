#!/usr/bin/python3
"""script"""

"""
    THOUGHT PROCESS
        n(log(n))-> not worth sorting
        loop and keep track max -> O(n)
        loop and reduce half of run time-> still O(n)
"""


def find_peak(list_of_integers):
    """BRUTE force"""
    max_i = None
    for i in list_of_integers:
        if max_i is None or max_i < i:
            max_i = i
    return max_i
