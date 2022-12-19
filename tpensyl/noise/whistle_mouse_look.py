from talon import Module, Context, actions, noise, ctrl
from math import log

mod = Module()
mod.tag("whistle_mouse_look", desc="move cursor with a whistle, y=power, x=f0") 
 
ctx = Context()
ctx.matches = """
tag: user.whistle_mouse_look
"""

# initialize
ts = 0
stop_ts = 0

pause_threshold = .3

# y axis based on power (volume)
power_deadzone = (250, 400)
min_delta_y = 1
speed_scaler_y = .02

# x axis based on frequency
# range is about from A#4-A#5 (466.16-932.33)
# halfway is E5=659.25
min_freq = 466.16
neutral_freq = 659.25
max_freq = 932.33
min_pitch = log(min_freq)
neutral_log = log(neutral_freq)
max_pitch = log(max_freq) 

max_speed = 10 #30 for talon a, 10 for mouse_event
speed_scaler_x = max_speed / (max_pitch - neutral_log)


use_static_scale = True

@ctx.action_class('user')
class WhistleActions:
    def whistle_start(ts:float, power:float, f0:float, f1:float, f2:float):
        """for debugging"""
        print("whistle start",[int(x) for x in (10*ts, power, f0, f1, f2)])
        #actions.user.whistle_repeat(ts, power, f0, f1, f2)
        if ts - stop_ts < pause_threshold:
            print("continue")
            return

    def whistle_stop(ts:float, power:float, f0:float, f1:float, f2:float):
        """for debugging"""
        print("whistle stop ",[int(x) for x in (10*ts, power, f0, f1, f2)])
        global stop_ts
        stop_ts = ts 
        ctrl.mouse_click(0)

    def whistle_repeat(ts:float, power:float, f0:float, f1:float, f2:float): 
        """for debugging"""
        f = f0

        base_x = neutral_log
        
        delta_x = (log(f) - base_x) * speed_scaler_x
        
        if power > power_deadzone[1]:
            delta_y = (power - power_deadzone[1]) * speed_scaler_y + min_delta_y
        elif power < power_deadzone[0]:
            delta_y = (power - power_deadzone[0]) * speed_scaler_y - min_delta_y
        else:
            delta_y = 0

        mouse_move(delta_x, -delta_y)
        print("whistle cont ", [int(x) for x in [10*ts, power, f0, f1, f2]])

import win32api, win32con
def mouse_move(x, y):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,int(x),int(y),0,0)
    # with talon, but might not work in a game
    # mouse_pos = ctrl.mouse_pos()
    # x = mouse_pos[0] + delta*speed_scaler_x
    # y = mouse_pos[1]
    # ctrl.mouse_move(x, y)