#!/usr/bin/python3
"""Class Square."""


class Square:
    """Class square."""

    def __init__(self, size=0):
        """Initialize a square instance

        Args:
            size (int): size
        """
        self.size = size

    @property
    def size(self):
        """Get/set """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area"""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Define  == comparision """
        return self.area() == other.area()

    def __ne__(self, other):
        """Define  != comparison """
        return self.area() != other.area()

    def __lt__(self, other):
        """Define  < comparison """
        return self.area() < other.area()

    def __le__(self, other):
        """Define  <= comparison """
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define  > comparison """
        return self.area() > other.area()

    def __ge__(self, other):
        """Define  >= compmarison """
        return self.area() >= other.area()
