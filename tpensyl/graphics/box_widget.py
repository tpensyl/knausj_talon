from talon import Module, Context, canvas, screen, ui, actions, ctrl
from talon.skia import Paint, Rect
from talon.skia.util import Color
mod = Module()

widget = None

@mod.action_class
class BoxWidgetActions:
    def init_box_widget():
        "override this method to create widget"
        close_widget()

    def set_box_widget(x1: int, y1: int, x2: int, y2: int, col: str = "aaaaaaaa"):
        "public method to create box"
        close_widget()
        global widget
        widget = BoxWidget(x1, y1, x2, y2, col)

    def get_widget():
        "returned the widget for direct manipulation"
        print(str(widget), "what the water weather")
        return widget

    def close_widget():  
        "removed the box"
        close_widget()
    
def close_widget():
    print("clothes widget")
    global widget
    if widget:
        widget.close()
        widget = None

class BoxWidget:
    def __init__(self, x1, y1, x2, y2, col):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.col = col

        self.screen = ui.screens()[0]
        self.c = canvas.Canvas.from_screen(self.screen)
        self.draw_method = self.on_draw_thick_grid
        self.c.register("draw", self.draw_method)

    def on_draw_simple(self, c):
        c.paint.color = self.col
        rect = Rect(self.x1, self.y1, self.x2 - self.x1, self.y2 - self.y1)
        c.draw_rect(rect)

    def on_draw_thick_grid(self, c):
        grain = 8
        grainY = 8
        blur = 0
        width = self.x2 - self.x1
        height = self.y2 - self.y1
        rect = Rect(self.x1, self.y1, width, height)
        img = screen.capture_rect(rect)
        bitmap = img.to_bitmap()
         
        for x in range(0, width, grain-1):
            col1 = bitmap.get_pixel(x + int(grain/2), self.y2 - self.y1 - 1)
            col2 = bitmap.get_pixel(x + int(grain/2), 0)
            for y in range(1, height - 1 - grainY, grainY):
                c.paint.color = average_colors(col1, col2, x=y/height, alpha=1)
                rect = Rect(self.x1 + x - blur, self.y1 + y, grain + blur, grainY)
                c.draw_rect(rect)


    def on_draw_thick_bars(self, c):
        width = 20
        for x in range(self.x1, self.x2, width):
            c.paint.color = screen.get_pixel(x, self.y2)
            # c.draw_line(x, self.y1, x, self.y2)
            rect = Rect(x, self.y1, width, self.y2 - self.y1)
            c.draw_rect(rect)

    def close(self):
        self.c.unregister("draw", self.draw_method)
        self.c.close()
        self.c = None

def average_colors(c1, c2, x=.5, alpha=.5):
    return Color.from_components(
        int(x * c1.r + (1 - x) * c2.r),
        int(x * c1.g + (1 - x) * c2.g),
        int(x * c1.b + (1 - x) * c2.b),
        int(alpha * 255))

def on_app_switch(app):
    actions.user.init_box_widget()


ui.register("app_activate", on_app_switch)
