import os
import sys
from math import pi


class Circle:
    def __init__(self, radius, fill='red', stroke='black'):
        self._radius = radius # private/protected
        self._fill = fill
        self._stroke = stroke

    @property
    def radius(self): # public access for _radius; read-only
        return self._radius

    def calculate_area(self):
        """Calculates the area"""
        return pi * self._radius ** 2

    @property
    def area(self):
        return self.calculate_area()

    def __len__(self):
        return int(2 * pi * self._radius)

    def __call__(self):
        return "I am a circle!"

    def __repr__(self):
        return f"Circle({self._radius}, fill={self._fill}, stroke={self._stroke})"


def main():
    circle = Circle(5.0, fill='orange', stroke='red')
    print(f"area = {circle.calculate_area()}")
    print(f"area = {circle.area}")
    print(f"circumference is {len(circle)}")
    print(circle())
    print(repr(circle))
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
