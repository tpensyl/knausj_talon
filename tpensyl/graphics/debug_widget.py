from talon import Module, canvas, screen, ui, cron
from talon.skia import Paint, Rect
from talon.canvas import Canvas
from time import time

mod = Module()
mod.tag("debug_widget", desc="allow print data on screen real time")

@mod.action_class
class DebugWidgetActions:
    def set_debug_coordinates(x: float, y: float):
        "set text location"
        dw.x = x
        dw.y = y

    def set_debug_text(text: any):
        "draw text to screen"
        dw.set_text(str(text))

    def start_stopwatch():
        "display a stopwatch"
        dw.start_stopwatch()

    def clear_stopwatch():
        "display a stopwatch"
        dw.set_text("")


class DebugWidget:
    def __init__(self):
        self.text_size = 40
        self.x = 10
        self.y = self.text_size

        self.text = ""
        self.expire_time = time()
        self.expire_job = None

        self.last_update = time()
        self.vanish_sec = 4
        self.vanish_sec_str = sec_to_cron_str(self.vanish_sec)

        screen = ui.screens()[0]
        c = canvas.Canvas.from_screen(screen)
        c.register("draw", self.on_draw)

        #cron.intervl("3s")

    def on_draw(self, c):
        c.paint.color = "ff2233bb"
        c.paint.textsize = self.text_size
        c.draw_text(self.text, self.x, self.y)

    def set_text(self, text):
        self.stop_stopwatch()
        self.text = text
        self.expire_time = time() + self.vanish_sec
        if not self.expire_job:
            self.expire_job = cron.after(self.vanish_sec_str, self.clear_text)

    def clear_text(self):
        time_remaining = self.expire_time - time()
        if time_remaining <= .030:
            self.text = ""
            self.expire_job = None
        else:
            cron.after(sec_to_cron_str(time_remaining), self.clear_text)

    def start_stopwatch(self):
        self.stop_stopwatch()
        global stopwatch_s, stopwatch_job
        stopwatch_s = 0
        stopwatch_job = cron.interval("100ms", self.increment_timer)

    def stop_stopwatch(self):  
        global stopwatch_job
        if stopwatch_job:
            cron.cancel(stopwatch_job)
            stopwatch_job = None

    def increment_timer(self):
        global stopwatch_s
        stopwatch_s += .1
        dw.text = "{:5.1f}".format(stopwatch_s)  

stopwatch_job = None
stopwatch_s = 0


def sec_to_cron_str(sec):
    ms = int(sec * 1000)
    return str(ms) + "ms"

# this hogs cpu on Linux, even if unused
#dw = DebugWidget()
