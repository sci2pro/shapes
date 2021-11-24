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