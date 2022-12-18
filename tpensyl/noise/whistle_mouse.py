from talon import Module, Context, actions, noise, ctrl
from math import log

ctx = Context()
ctx.tags = ["user.whistle_mouse"]

mod = Module()
mod.tag("whistle_mouse", desc="move cursor with a whistle") 
 
# initialize
ts = 0
stop_ts = 0

pause_threshold = .3

# y axis based on power (volume)
neutral_power = 400
delta_y_threshold = 3
speed_scaler_y = -.02

# x axis based on frequency
# range is about from A#4-A#5 (466.16-932.33)
# halfway is E5=659.25
minimum_freq = 466.16
neutral_freq = 659.25
maximum_freq = 932.33
minimum_log = log(minimum_freq)
neutral_log = log(neutral_freq)
maximum_log = log(maximum_freq) 

max_speed = 10 #30 for talon a, 10 for mouse_event
speed_scaler_x = max_speed / (maximum_log - neutral_log)


use_static_scale = True

# @mod.action_class
@ctx.action_class('self')
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
        

    def whistle_repeat(ts:float, power:float, f0:float, f1:float, f2:float): 
        """for debugging"""
        f = f0

        base_x = neutral_log
        
        delta_x = (log(f) - base_x) * speed_scaler_x
        
        delta_y = (power - neutral_power) * speed_scaler_y
        
        if abs(delta_y) < delta_y_threshold:
            delta_y = 0 
        else:
            delta_y = delta_y
            #delta_y = (abs(delta_y) - delta_y_threshold) * abs(delta_y)/delta_y

        mouse_move(delta_x, delta_y)
        print("whistle cont ", [int(x) for x in [10*ts, power, f0, f1, f2]])

import win32api, win32con
def mouse_move(x, y):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,int(x),int(y),0,0)
    # with talon, but might not work in a game
    # mouse_pos = ctrl.mouse_pos()
    # x = mouse_pos[0] + delta*speed_scaler_x
    # y = mouse_pos[1]
    # ctrl.mouse_move(x, y)