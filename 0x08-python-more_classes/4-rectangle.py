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

            self.width = width
            self.height = height
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Property width to retrieve it

        Returns:
            width (int): The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter width of the rectangle

        Attributes:
            width (int): The width of the rectangle

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Property height to retrieve it

        Returns:
            height (int): The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter height of the rectangle

        Attributes:
            height (int): The height of the rectangle

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """
        A str method to print # in representation of number of h and w
        """

        string = ""

        if self.__width == 0 or self.__height == 0:
            return string

        else:
            for i in range(self.__height):
                for j in range(self.width):
                    string += '#'
                if i < self.__height - 1:
                    string += '\n'
            return string

    def __repr__(self):
        """
        provides __repr__ method for object rectangle

        Returns:+
            string (str): string to get
        """
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) +\
            ")"
