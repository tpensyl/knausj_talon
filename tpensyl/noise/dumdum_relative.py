from talon import Module, Context, actions, ctrl, cron
from math import log

mod = Module()
mod.tag("dumdum_look_relative", desc="move cursor with silly voice, y=power, x=f0") 
 
ctx = Context()
ctx.matches = """
os: windows
tag: user.dumdum_look_relative
"""

# initialize
frames_x = []
frames_y = []
stop_job = None

# y axis based on power (volume)
speed_scaler_x = .1

# x axis based on frequency
speed_scaler_y = 15

@ctx.action_class('user')
class DumdumActions:
    def dumdum_start(ts:float, power:float, f0:float, f1:float, f2:float):
        """dumdum_start"""
        #print("continue")
        if stop_job:
            cron.cancel(stop_job)
            return

        global x0, y0
        global frames_x, frames_y
        x0 = power
        y0 = log(f0)
        frames_x = [x0]
        frames_y = [y0]

        ctrl.mouse_click(0, down=True)

    def dumdum_stop(ts:float, power:float, f0:float, f1:float, f2:float):
        """dumdum_stop"""
        def do_stop():
            global stop_job
            ctrl.mouse_click(0,up=True)
            stop_job = None
        global stop_job
        if stop_job:
            cron.cancel(stop_job)
        stop_job = cron.after("200ms", do_stop) 

    def dumdum_repeat(ts:float, power:float, f0:float, f1:float, f2:float): 
        """dumdum_repeat"""
        global frames_x, frames_y
        x = power
        y = log(f0)
        if len(frames_x) < 5:
            frames_x += [x]
            frames_y += [y]
            return

        x0 = sum(frames_x) / len(frames_x)
        y0 = sum(frames_y) / len(frames_y)
        delta_x = (x - x0) * speed_scaler_x
        delta_y = (y - y0) * speed_scaler_y
        
        mouse_move(delta_x, -delta_y)
        actions.user.dumdum_widget(delta_x, -delta_y)
        #print("eee cont ", [int(x) for x in [10*ts, power, f0, f1, f2]])

    def mouse_move(dx, dy):
        import win32api, win32con
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,int(dx),int(dy),0,0)