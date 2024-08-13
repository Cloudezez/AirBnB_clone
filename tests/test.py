#!/usr/bin/python3

from python1 import Example
import unittest
import sys
import os

# Add the parent directory to the system path
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
)


class TestExample(unittest.TestCase):
    """
    Test cases for the Example class.
    """

    def setUp(self):
        """
        Set up an Example instance for testing.
        """
        self.example = Example(10)

    def test_get_value(self):
        """
        Test the get_value method of Example class.
        """
        self.assertEqual(self.example.get_value(), 10)
