#!/usr/bin/python3
"""number_of_lines"""


def number_of_lines(filename=""):
    """number_of_lines."""
    lines = 0
    with open(filename) as f:
        for line in f:
            lines += 1
    return lines
