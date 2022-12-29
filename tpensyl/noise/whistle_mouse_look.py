from talon import Module, Context, actions, ctrl, cron
from math import log, sin, cos, pi

mod = Module()
mod.tag("whistle_mouse_look", desc="move cursor with a whistle, y=power, x=f0") 
 
ctx = Context()
ctx.matches = """
os: windows
and tag: user.whistle_mouse_look
"""

# initialize
stop_job = None

pause_threshold = .4

# y axis based on power (volume)
neutral_power = 330
min_delta_y = 1
speed_scaler_y = .03

# x axis based on frequency
# range is about from A#4-A#5 (466.16-932.33)
# halfway is E5=659.25
min_freq = 466.16
neutral_freq = 659.25
max_freq = 932.33
min_pitch = log(min_freq)
max_pitch = log(max_freq)
mid_pitch = (min_pitch + max_pitch) / 2

max_speed = 3
speed_scaler_x = max_speed / (max_pitch - mid_pitch)

@ctx.action_class('user')
class WhistleActions:
    def whistle_start(ts:float, power:float, f0:float, f1:float, f2:float):
        """whistle_start debugging"""
        if stop_job:
            cron.cancel(stop_job)
            return

        ctrl.mouse_click(0, down=True)
    
    def whistle_stop(ts:float, power:float, f0:float, f1:float, f2:float):
        """whistle_stop debugging"""
        def do_stop():
            global stop_job
            ctrl.mouse_click(0,up=True)
            stop_job = None
        global stop_job
        if stop_job:
            cron.cancel(stop_job)
        stop_job = cron.after("200ms", do_stop) 

    def whistle_repeat(ts:float, power:float, f0:float, f1:float, f2:float): 
        """for debugging"""
        f = f0

        base_x = mid_pitch
        
        delta_x = (log(f) - base_x) * speed_scaler_x
        
        delta_y = (power - neutral_power) * speed_scaler_y
        delta_x, delta_y = map_radial(delta_y, delta_x * pi)

        mouse_move(delta_x, -delta_y)
        actions.user.dumdum_widget(delta_x, -delta_y)
        # print("whistle cont ", [int(x) for x in [10*ts, power, f0, f1, f2]])

def map_radial(r, θ):
    x = r * sin(θ)
    y = r * cos(θ)
    return x, y

import win32api, win32con
def mouse_move(dx, dy):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,int(dx),int(dy),0,0)
    