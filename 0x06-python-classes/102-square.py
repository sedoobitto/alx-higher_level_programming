#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Compare if square is equal to another by area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare if square is not equal to another by area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Compare if square is less than another by area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Compare if square is less than or equal to another by area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Compare if square is greater than another by area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare if square is greater than or equal to another by area."""
        return self.area() >= other.area()
