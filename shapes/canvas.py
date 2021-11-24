import turtle



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
