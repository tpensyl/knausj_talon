from talon import Module, Context, canvas, screen, ui, actions, ctrl
from talon.skia import Paint, Rect, Path
from talon.skia.util import Color
mod = Module()

overlay = None
@mod.action_class
class OverlayActions:
    def init_overlay():
        "override this method to create widget"
        global overlay
        overlay = LineWidget(1, -1080, 1920, 0)
        overlay = LineWidget(1, -1080, 1920, 500)
        overlay = LineWidget(-1000, -1000, 1000, 1000)
        overlay = LineWidget(-1000, 1000, -1000, 1000)
        overlay = LineWidget(-500, 1000, -1300, 1000) 
    
class LineWidget:
    def __init__(self, x1, y1, x2, y2, relative=True):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        screen = ui.screen_containing(*ctrl.mouse_pos())
        # screen = ui.screens()[0]
        print("scrren.rect",screen.rect)
        print(ctrl.mouse_pos())
        c = canvas.Canvas.from_rect(Rect(-1000,1000,-2000,2000))
        c = canvas.Canvas.from_screen(screen)

        #c = canvas.Canvas.from_screen(screen)
        c.register("draw", self.draw)

    def draw(self, c):
        c.paint.style = c.paint.Style.STROKE
        c.paint.stroke_width = 20
        c.paint.color = Color.from_components(0, 0, 0, 200)
        c.draw_line(self.x1, self.y1, self.x2, self.y2)
        # rect = Rect(self.x1, self.y1, self.x2 - self.x1, self.y2 - self.y1)
        # c.draw_rect(rect)
        # c.draw_rect(Rect(0,0,2000,2000))
        pass

def on_app_switch(app):
    actions.user.init_overlay()

# ui.register("app_activate", on_app_switch)