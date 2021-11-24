import os
import sys
import turtle
from math import pi

import yaml

turtle.tracer(False)


class Circle:
    def __init__(self, radius, fill='red', stroke='black', at=(0, 0)):
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
        pen.goto(self.left, self.top)
        pen.down()
        pen.goto(self.left, self.bottom)
        pen.goto(self.right, self.bottom)
        pen.goto(self.right, self.top)
        pen.goto(self.left, self.top)
        pen.up()


class Canvas(turtle.TurtleScreen):
    def __init__(self, width, height, bg='white'):
        self._cv = turtle.getcanvas()
        super().__init__(self._cv)
        self.screensize(width, height, bg=bg)
        self._width = width
        self._height = height
        self._bg = bg
        self._pen = turtle.Turtle()

    def draw_axes(self):
        # self._pen.speed(0)
        self._pen.up()
        self._pen.goto(0, self._height / 2)
        self._pen.down()
        self._pen.goto(0, -self._height / 2)
        self._pen.up()
        self._pen.goto(-self._width / 2, 0)
        self._pen.down()
        self._pen.goto(self._width / 2, 0)
        self._pen.up()
        self._pen.home()
        # self._pen.goto(-self._width / 2, -self._height / 2)

    def draw_grid(self, colour='#00ff99', hstep=50, vstep=50):
        # self._pen.speed(0)
        original_pen_colour = self._pen.pencolor()
        self._pen.color(colour)
        # vertical grids
        self._pen.up()
        for hpos in range(-500, 500 + hstep, hstep):
            self._pen.goto(hpos, 350)
            self._pen.down()
            self._pen.goto(hpos, -350)
            self._pen.up()
        # horizontal grids
        for vpos in range(-350, 350 + vstep, vstep):
            self._pen.goto(-500, vpos)
            self._pen.down()
            self._pen.goto(500, vpos)
            self._pen.up()
        # reset
        self._pen.pencolor(original_pen_colour)

    def write(self, text, *args, **kwargs):
        text.write(self._pen, *args, **kwargs)

    def draw(self, shape):
        shape.draw(self._pen)


class Text:
    def __init__(self, text, at=(0, 0)):
        self._text = text
        self._at = at

    def write(self, pen, *args, **kwargs):
        pen.up()
        pen.goto(self._at)
        pen.down()
        pen.write(self._text, *args, **kwargs)
        pen.up()


def main():
    circle = Circle(50, fill='orange', stroke='red')
    print(f"area = {circle.calculate_area()}")
    print(f"area = {circle.area}")
    print(f"circumference is {len(circle)}")
    print(circle())
    print(repr(circle))

    my_dict = {
        'key': {
            'inside_dict': [5, 6, 7, 8]
        }
    }

    my_yaml = yaml.dump(my_dict)
    print(my_yaml)

    print(circle)

    yaml_circle = """\
circle:
  at: !!python/tuple
  - 0
  - 0
  fill: orange
  radius: 5.0
  stroke: red"""
    my_circle = Circle.from_yaml(yaml_circle)

    pen = turtle.Turtle()  # we draw with a turtle
    text = Text("This was written by a turtle!", at=(20, -50))
    print(text)
    text.write(pen, font=('Arial', 30, 'bold'))

    circle.draw(pen)

    # quad
    quad = Quadrilateral(200, 60, at=(215, -5))
    print(f"vertices = {quad.vertices}")
    quad.draw(pen)

    # canvas
    canvas = Canvas(1000, 700)
    canvas.draw_axes()
    canvas.draw_grid()
    canvas.write(text)
    # user
    canvas.draw(circle)

    turtle.done()

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
