from talon import Module, Context, canvas, screen, ui
#from talon.types.point import Point2d
from talon.skia import Paint, Rect
from talon.canvas import Canvas

mod = Module()
mod.tag("aim_widget", desc="visual indicator for aim modules")

# doesn't actually work for gating the raw python at bottom
ctx = Context()
ctx.matches = """
tag: user.aim_widget
"""

global radial_indicator
radial_indicator = False

@mod.action_class
class DumdumWidgetWrapper:
    def dumdum_widget(x: float, y: float):
        "draw an indicator on the stream"
        dw.dx = x * 30
        dw.dy = y * 30
    
    def set_radial_indicator(b: bool):
        "setter"
        global radial_indicator
        radial_indicator = True
        
class DumdumWidget:
    def __init__(self):
        self.dx = 0
        self.dy = 0

        screen = ui.screens()[0]
        c = canvas.Canvas.from_screen(screen)
        c.register("draw", self.on_draw)

    def on_draw(self, c):
        c.paint.color = "ff2233bb"

        center_x = c.x + c.width / 2
        center_y = c.y + c.height / 2
        target_x = center_x + self.dx
        target_y = center_y + self.dy
        target_x = max(0, min(c.width,  target_x))
        target_y = max(0, min(c.height, target_y))
        if radial_indicator:
            dcx = self.dx - center_x
            dcy = self.dy - center_y
            sz = .3
            c.draw_line(target_x, target_y, target_x - sz*self.dx, target_y - sz*self.dy)
        
        size = 12
        rect = Rect(target_x - size / 2, target_y - size / 2, size, size)
        c.draw_rect(rect)
        # rect = Rect(center_x - size / 2, center_y - size / 2, size, size) 
        # c.draw_rect(rect)

    

#dw = DumdumWidget()
