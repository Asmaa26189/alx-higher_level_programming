#!/usr/bin/python3
"""Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square."""
    def __init__(self, size, x=0, y=0, id=None):
        """init."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """set/get size."""
        return self.width

    @size.setter
    def size(self, value):
        """size."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.height = value
        self.width = value

    def update(self, *args, **kwargs):
        """update."""
        index = 0
        if len(args) > 0:
            for arg in args:
                if index == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    self.id = arg
                if index == 1:
                    self.size = arg
                if index == 2:
                    self.x = arg
                if index == 3:
                    self.y = arg
                index += 1
        elif len(kwargs) > 0:
            if 'id' in kwargs:
                if kwargs['id'] is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def __str__(self):
        """str."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def to_dictionary(self):
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
    
