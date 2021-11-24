from math import pi

import yaml


class Circle:
    def __init__(self, radius, fill='red', stroke='black', at=(0, 0)):
        try:
            assert radius > 0
        except AssertionError:
            raise ValueError(f"invalid radius: {radius}")
        self._radius = radius  # private/protected
        self._fill = fill
        self._stroke = stroke
        self._at = at

    @property
    def radius(self):  # public access for _radius; read-only
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

    def __str__(self):
        string = yaml.dump({
            'circle': {
                'radius': self._radius,
                'fill': self._fill,
                'stroke': self._stroke,
                'at': self._at
            }
        })
        return string

    @property
    def circumference(self):
        return 2 * pi * self._radius

    @classmethod
    def from_yaml(cls, string):
        """Create a circle from a YAML string"""
        circle_dict = yaml.load(string, Loader=yaml.Loader)['circle']
        print(circle_dict)
        obj = cls(circle_dict['radius'], fill=circle_dict['fill'], stroke=circle_dict['stroke'], at=circle_dict['at'])
        return obj

    def draw(self, pen, *args, **kwargs):
        """Draw a circle"""
        if pen.isdown():
            pen.up()
        pen.goto(*self._at)
        pen.down()
        pen.begin_fill()
        pen.pencolor(self._stroke)
        pen.fillcolor(self._fill)
        pen.circle(self._radius, *args, **kwargs)
        pen.end_fill()
        pen.up()


class Quadrilateral:
    def __init__(self, width, height, fill='blue', stroke='red', at=(0, 0)):
        self._width = width
        self._height = height
        self._fill = fill
        self._stroke = stroke
        self._at = at

    @property
    def left(self):
        return self._at[0] - self._width / 2

    @property
    def top(self):
        return self._at[1] + self._height / 2

    @property
    def right(self):
        return self._at[0] + self._width / 2

    @property
    def bottom(self):
        return self._at[1] - self._height / 2

    @property
    def vertices(self):
        """Starting from the top left counter clockwise"""
        return [
            (self.left, self.top),
            (self.left, self.bottom),
            (self.right, self.bottom),
            (self.right, self.top),
        ]

    def draw(self, pen, *args, **kwargs):
        pen.up()
        pen.pencolor(self._stroke)
        pen.fillcolor(self._fill)
        pen.begin_fill()
        pen.goto(self.left, self.top)
        pen.down()
        pen.goto(self.left, self.bottom)
        pen.goto(self.right, self.bottom)
        pen.goto(self.right, self.top)
        pen.goto(self.left, self.top)
        pen.end_fill()
        pen.up()