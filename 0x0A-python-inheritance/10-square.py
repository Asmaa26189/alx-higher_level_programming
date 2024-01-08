#!/usr/bin/python3
"""Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square from Rectangle."""

    def __init__(self, size):
        """__init__ """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
