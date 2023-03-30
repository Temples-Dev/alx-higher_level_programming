#!/usr/bin/python3
""" Access and update private attribute"""


class Square:
    """private instance :size"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    """Public instance method: def area(self)"""
    def area(self):
        return self.__size ** 2

    """Public instance method: == """
    def __eq__(self, other):
        return self.area() == other.area()

    """Public instance method: != """
    def __ne__(self, other):
        return self.area() != other.area()

    """Public instance method: > """
    def __gt__(self, other):
        return self.area() > other.area()

    """Public instance method: >= """
    def __ge__(self, other):
        return self.area() >= other.area()

    """Public instance method: <"""
    def __lt__(self, other):
        return self.area() < other.area()

    """Public instance method: <= """
    def __le__(self, other):
        return self.area() <= other.area()
