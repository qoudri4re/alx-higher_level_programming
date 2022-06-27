#!/usr/bin/python3
"""Define a class Rectangle"""


class Rectangle:
    """ Class that defines a rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes the instance object
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """returns the value of the width
        Returns:
            width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """method that defines the width
        Args:
            value: width of the rectangle
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns the value of the height
        Returns:
            height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """method that defines the height
        Args:
            value: height of the rectangle
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than 0
        """
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """method that returns the area of the rectangle
        Returns:
            area
        """
        return self.width * self.height

    def perimeter(self):
        """method that returns the perimeter of rectangle
        Returns:
            perimetr
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * self.width + 2 * self.height

    def __str__(self):
        """returns the rectangle with #
        Returns:
            #magic
        """
        return_val = ""
        if self.width == 0 or self.height == 0:
            return return_val

        for i in range(self.height):
            i += 0
            return_val += (str(self.print_symbol)) * self.width + "\n"
        return return_val[:-1]

    def __repr__(self):
        """method that returns string representation of the instance
        Returns:
            string representation
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """method that prints a message when an instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """method that returns the bigger rectangle based on area
        Args:
            rect_1: Rectangle 1
            rect_2: Rectangle 2
        Raises:
            TypeError: when some argument passed is not an instance of the
            rectangle class
        Returns:
            the bigger rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        elif rect_1.area() == rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """method that returns a new instance of Rectangle class
        Args:
            cls: rectangle class
            size: rectangle width and rectangle height
        Returns:
            a new instance of rectangle class
        """
        return cls(size, size)
