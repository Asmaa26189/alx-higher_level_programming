#!/usr/bin/python3
"""Class Square"""


class Square:
    """Class square"""

    def __init__(self, size):
        """Initialize a square instance

        Args:
            size (int): size
        """
        self.size = size

    @property
    def size(self):
        """Get/set square size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print square with # """
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
