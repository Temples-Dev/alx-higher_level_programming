#!/usr/bin/python3
"""Area of a square"""


class Square:
    """Area of a square"""
    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    """Public instance method: def area(self): that returns the current square area"""
    def area(self):

        return (self.__size ** 2)





    # def __init__(self, size=0):
    #     if type(size) != int:
    #         raise TypeError("size must be an integer")
    #     elif size < 0:
    #         raise ValueError("size must be >= 0")
    #     else:
    #         self.__size = size


    # def area(self):
    #     return (self.__size ** 2)
