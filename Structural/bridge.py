class DrawingApiOne:
    def draw_circle(self, x,y, radius):
        print("CIRCLE DRAWN BY API 1", x, y, radius)

class DrawingApiTwo:
    def draw_circle(self, x,y, radius):
        print("CIRCLE DRAWN BY API 2",  x, y, radius)

class Circle:
    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percent):
        self._radius *= percent

c1 = Circle(1, 2, 3 , DrawingApiOne())
c1.scale(2)
c1.draw()