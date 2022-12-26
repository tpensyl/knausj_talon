from talon import Module, Context, actions, ctrl, cron
from math import log

mod = Module()
mod.tag("dumdum_look", desc="move cursor with silly voice, y=power, x=f0") 
 
ctx = Context()
ctx.matches = """
tag: user.dumdum_look
"""

# initialize
ts = 0
stop_ts = 0

pause_threshold = .3

# y axis based on power (volume)
power_deadzone = (225, 240)
min_delta_y = 1
speed_scaler_y = .05

# x axis based on frequency
min_freq = 200
max_freq = 400
min_pitch = log(min_freq)
max_pitch = log(max_freq)
mid_pitch = (min_pitch + max_pitch) / 2

max_speed = 20 * .5
speed_scaler_x = max_speed / (max_pitch - mid_pitch)

@ctx.action_class('user')
class DumdumActions:
    def dumdum_start(ts:float, power:float, f0:float, f1:float, f2:float):
        """for debugging"""
        print("whistle start",[int(x) for x in (10*ts, power, f0, f1, f2)])
        if ts - stop_ts < pause_threshold:
            print("continue")
            if stop_job:
                cron.cancel(stop_job)
            return

        ctrl.mouse_click(0,down=True)

    def dumdum_stop(ts:float, power:float, f0:float, f1:float, f2:float):
        """for debugging"""
        print("whistle stop ",[int(x) for x in (10*ts, power, f0, f1, f2)])
        global stop_ts, stop_job
        stop_ts = ts 
        stop_job = cron.after("150ms", do_stop)
        print("eee stop ", [int(x) for x in [10*ts, power, f0, f1, f2]])

    def dumdum_repeat(ts:float, power:float, f0:float, f1:float, f2:float): 
        """for debugging"""
        f = f0

        base_x = mid_pitch
        
        delta_x = (log(f) - base_x) * speed_scaler_x
        
        if power > power_deadzone[1]:
            delta_y = (power - power_deadzone[1]) * speed_scaler_y + min_delta_y
        elif power < power_deadzone[0]:
            delta_y = (power - power_deadzone[0]) * speed_scaler_y - min_delta_y
        else:
            delta_y = 0

        dw.x = delta_x * 30
        dw.y = -delta_y * 30
        mouse_move(delta_x, -delta_y)
        print("eee cont ", [int(x) for x in [10*ts, power, f0, f1, f2]])

def do_stop():
    print("do_stop")
    ctrl.mouse_click(0,up=True)


from talon import canvas, screen, ui
from talon.types.point import Point2d
from talon.skia import Paint, Rect

class DumdumWidget:
    def __init__(self):
        self.mcanvas = None
        self.center = None
        self.x = 0
        self.y = 0

    def initialize_widget(self):
        screen = ui.screens()[0]
        self.center = screen.rect.center
        self.mcanvas = canvas.Canvas.from_screen(screen)
        self.mcanvas.register("draw", self.draw)

    def draw(self, canvas):
        paint = canvas.paint
        paint.color = "ff2233bb"
        #point = Point2d(5, 20)
        #canvas.draw_line(5, 20, 200, 400)
        self.draw_target(canvas, self.x, self.y)
        # debug(canvas)1
    
    def draw_target(self, canvas, x, y):
        size = 20
        target_x = self.center.x + x - size / 2
        target_y = self.center.y + y - size / 2
        target_x = max(0, min(2*self.center.x, target_x))
        target_y = max(0, min(2*self.center.y, target_y))
        rect = Rect(target_x, target_y, size, size)
        canvas.draw_rect(rect)



should_print = True
def print_once(object):
    global should_print
    if should_print:
        should_print = False
        print([method_name for method_name in dir(object)
                  if callable(getattr(object, method_name))])

dw = DumdumWidget()
dw.initialize_widget()

import win32api, win32con
def mouse_move(dx, dy):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,int(dx),int(dy),0,0)
    # with talon, but might not work in a game
    # mouse_pos = ctrl.mouse_pos()
    # x = mouse_pos[0] + delta*speed_scaler_x
    # y = mouse_pos[1]
    # ctrl.mouse_move(x, y)