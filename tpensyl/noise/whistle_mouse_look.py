from talon import Module, Context, actions, ctrl, cron
from math import log

mod = Module()
mod.tag("whistle_mouse_look", desc="move cursor with a whistle, y=power, x=f0") 
 
ctx = Context()
ctx.matches = """
tag: user.whistle_mouse_look
"""

# initialize
stop_job = None

pause_threshold = .4

# y axis based on power (volume)
power_deadzone = (300, 320)
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

max_speed = 50
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
        
        if power > power_deadzone[1]:
            delta_y = (power - power_deadzone[1]) * speed_scaler_y + min_delta_y
        elif power < power_deadzone[0]:
            delta_y = (power - power_deadzone[0]) * speed_scaler_y - min_delta_y
        else:
            delta_y = 0

        mouse_move(delta_x, -delta_y)
        actions.user.dumdum_widget(delta_x, -delta_y)
        # print("whistle cont ", [int(x) for x in [10*ts, power, f0, f1, f2]])

import win32api, win32con
def mouse_move(dx, dy):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,int(dx),int(dy),0,0)