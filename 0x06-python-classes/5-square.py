#!/usr/bin/python3
"""Printing a square"""


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

    """prints in stdout the square with the character #"""
    def my_print(self):
        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
