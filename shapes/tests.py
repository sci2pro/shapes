import unittest

from .shapes import Circle
from math import pi


class TestCircle(unittest.TestCase):  # all our tests are subclasses of TestCase
    def test_init(self):
        """Test initialisation of a circle"""
        radius = 60
        circle = Circle(radius)
        self.assertEqual(radius, circle.radius)

    def test_invalid(self):
        """circles must be real"""
        with self.assertRaises(ValueError):
            Circle(-47)

    def test_circumference(self):
        """We have the right value of circ."""
        radius = 10
        circle = Circle(radius)
        self.assertEqual(2 * pi * radius, circle.circumference)


