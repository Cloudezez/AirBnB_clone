#!/usr/bin/python3

"""
This module provides an example class with a simple method.
"""


class Example:
    """
    This class demonstrates a simple Python class with a method.
    """

    def __init__(self, value):
        """
        Initialize the Example class with a value.

        Args:
            value (int): The value to initialize.
        """
        self.value = value

    def get_value(self):
        """
        Get the value of the Example instance.
        Returns:
            int: The value of the instance.
        """
        return self.value


if __name__ == "__main__":
    example = Example(10)
    print(example.get_value())
