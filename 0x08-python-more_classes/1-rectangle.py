#!/usr/bin/python3
"""rectangle"""

class Rectangle:
    """rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize rectangle instance

        Args:
            width (int): width
            height (int): height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set width property"""
        return self.__width
        
    @property
    def height(self):
        """Get/set height property"""
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value)
        if not isinstance(value, int):
            raise TypeError("heighr must be integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
