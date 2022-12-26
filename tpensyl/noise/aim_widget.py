from talon import Module, canvas, screen, ui
#from talon.types.point import Point2d
from talon.skia import Paint, Rect
from talon.canvas import Canvas

mod = Module()

@mod.action_class
class DumdumWidgetWrapper:
    def dumdum_widget(x: float, y: float):
        "draw an indicator on the stream"
        dw.dx = x
        dw.dy = y
        
class DumdumWidget:
    def __init__(self):
        self.dx = 0
        self.dy = 0

        screen = ui.screens()[0]
        c = canvas.Canvas.from_screen(screen)
        c.register("draw", self.on_draw)

    def on_draw(self, c):
        size = 20
        c.paint.color = "ff2233bb"

        center_x = c.x + c.width / 2
        center_y = c.y + c.height / 2
        target_x = center_x + self.dx - size / 2
        target_y = center_y + self.dy - size / 2
        target_x = max(0, min(c.width,  target_x))
        target_y = max(0, min(c.height, target_y))
        rect = Rect(target_x, target_y, size, size)
        c.draw_rect(rect)

dw = DumdumWidget()
