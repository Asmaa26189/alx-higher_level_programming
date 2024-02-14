#!/usr/bin/python3
"""Rectangle"""
from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        """width."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """set/get Width."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("Type must be int")
        if value <= 0:
            raise ValueError("value must be >= zero")
        self.__width = value

    @property
    def height(self):
        """set/get height."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("type must be int")
        if value <= 0:
            raise ValueError("value must be >= zero")
        self.__height = value

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """set/get y"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("type must be int")
        if value < 0:
            raise ValueError("value must be >= zero")
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(0, self.y)]
        for h in range(0, self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")
    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
    def update(self, *args, **kwargs):
        index = 0
        if args and len(args) != 0:
            for arg in args:
                if index == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                if index == 1:
                    self.width = arg
                if index == 2:
                    self.height = arg
                if index == 3:
                    self.x = arg
                if index == 4:
                    self.y = arg
                index += 1

        elif kwargs and len(kwargs) != 0:
            if 'id' in kwargs:
                if kwargs['id'] is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                else:
                    self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        return {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height,
                                                         'width': self.width}
