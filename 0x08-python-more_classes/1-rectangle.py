#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
created - Sunday January 14 2024

@author: Ab Yahaya
"""


class Rectangle:
    """
    a rcatngle class with instance variables

    Attributes:
        empty
    """

    def __init__(self, width=0, height=0):
        """
        init method with:
        Attributes:
            width - width of rectangle
            height - height of rectangle
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value