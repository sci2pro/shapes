import os
import sys
import turtle

from shapes.canvas import Canvas
from shapes.shapes import Quadrilateral
from shapes.text import Text

turtle.tracer(False)


def main():
    #     circle = Circle(50, fill='orange', stroke='red')
    #     print(f"area = {circle.calculate_area()}")
    #     print(f"area = {circle.area}")
    #     print(f"circumference is {len(circle)}")
    #     print(circle())
    #     print(repr(circle))
    #
    #     my_dict = {
    #         'key': {
    #             'inside_dict': [5, 6, 7, 8]
    #         }
    #     }
    #
    #     my_yaml = yaml.dump(my_dict)
    #     print(my_yaml)
    #
    #     print(circle)
    #
    #     yaml_circle = """\
    # circle:
    #   at: !!python/tuple
    #   - 0
    #   - 0
    #   fill: orange
    #   radius: 5.0
    #   stroke: red"""
    #     my_circle = Circle.from_yaml(yaml_circle)
    #
    #     pen = turtle.Turtle()  # we draw with a turtle
    #     text = Text("This was written by a turtle!", at=(20, -50))
    #     print(text)
    #     text.write(pen, font=('Arial', 30, 'bold'))
    #
    #     circle.draw(pen)
    #
    #     # quad
    #     quad = Quadrilateral(200, 60, at=(215, -5))
    #     print(f"vertices = {quad.vertices}")
    #     quad.draw(pen)
    #
    #     # canvas
    #     canvas = Canvas(1000, 700)
    #     canvas.draw_axes()
    #     canvas.draw_grid()
    #     canvas.write(text)
    #     # user
    #     canvas.draw(circle)

    canvas = Canvas(1000, 700)
    gquad = Quadrilateral(
        200, 300, fill='#009a44', stroke='white', at=(-200, 0)
    )
    wquad = Quadrilateral(
        200, 300, fill='white', stroke='#dddddd', at=(0, 0)
    )
    oquad = Quadrilateral(
        200, 300, fill='#ff8200', stroke='white', at=(200, 0)
    )
    text = Text('IRELAND', at=(0, -250))
    canvas.draw(gquad)
    canvas.draw(wquad)
    canvas.draw(oquad)
    canvas.write(text, align='center', font=('Arial', 60, 'bold'))

    turtle.done()

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
