#!/usr/bin/python3

"""creates a class Rectangle that defines a rectangle"""


class Rectangle:
    """class of a rectangle"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """retrieve the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """used to set the width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """retieves the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """used to set the height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Gets area of rectangle"""
        return self.height * self.width

    def perimeter(self):
        """Gets perimeter of the rectangle"""
        if self.__width == 0 or self.__width == 0:
            return 0
        return 2 * (self.width + self.height)
