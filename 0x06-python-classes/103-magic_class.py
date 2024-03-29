#!/usr/bin/python3
""" ByteCode -> Python #5"""
import math


class MagicClass:
    """ Class"""
    def __init__(self, radius=0):
        """ initialize """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """area returned"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ circumference returned"""
        return 2 * math.pi * self.__radius
