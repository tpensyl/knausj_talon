from talon import Module, Context, actions, noise, ctrl
from math import log

ctx = Context()
ctx.matches = r"""
tag: user.whistle_mouse_swoop
"""

mod = Module()
mod.tag("whistle_mouse_swoop", desc="move cursor with a whistle, relative to the starting pitch")

# initialize
ts = 0
stop_ts = 0

# relative scaling, based on first sound
start_frames = []
delta_threshold = 100
speed_scaler_x = .1
pause_threshold = .3

neutral_power = 250
# range is about from A#4-A#5 (466.16-932.33)
# halfway is E5=659.25
minimum_freq = 466.16
maximum_freq = 932.33
minimum_log = log(minimum_freq)
maximum_log = log(maximum_freq) 

max_speed = 10 #30 for talon mouse, 10 for mouse_event
speed_scaler_x = max_speed / (maximum_log - neutral_log)
speed_scaler_y = -.05

@mod.action_class
class WhistleActions:

    def whistle_start(ts:float, power:float, f0:float, f1:float, f2:float):
        """for debugging"""
        print("whistle start",[int(x) for x in (10*ts, power, f0, f1, f2)])
        global start_frames, stop_ts
        if ts - stop_ts < pause_threshold:
            print("continue")
            return 
        
        f = f0
        start_frames = [log(f)]

    def whistle_stop(ts:float, power:float, f0:float, f1:float, f2:float):
        """for debugging"""
        print("whistle stop",[int(x) for x in (10*ts, power, f0, f1, f2)])
        global stop_ts
        stop_ts = ts 
        

    def whistle_repeat(ts:float, power:float, f0:float, f1:float, f2:float): 
        """for debugging"""
        # relative scaling; need to clean
        global start_frames 
        f = f0
        if len(start_frames) < 5:
            start_frames += [log(f)]

        base = sum(start_frames) / len(start_frames)
        
        delta_x = (log(f) - base) * speed_scaler_x
        
        delta_y = (power - neutral_power) * speed_scaler_y
        delta_y_threshold = 2

        if abs(delta_y) < delta_y_threshold:
            delta_y = 0 
        else:
            delta_y = (abs(delta_y) - delta_y_threshold) * abs(delta_y)/delta_y

        mouse_move(delta_x, delta_y)
        print("whistle", [int(x) for x in [power, f0, f1, f2, f]])

import win32api, win32con
def mouse_move(dx, dy):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,int(dx),int(dy),0,0)
    # with talon, but might not work in a game based on relative motion
    # mouse_pos = ctrl.mouse_pos()
    # x = mouse_pos[0] + dx
    # y = mouse_pos[1] + dy
    # ctrl.mouse_move(x, y)