from talon import Module, Context, actions, ctrl, cron
from math import log, sin, cos

mod = Module()
mod.tag("dumdum_look_radial", desc="move cursor with silly voice, y=power, x=f0") 
 
ctx = Context()
ctx.matches = """
os: windows
and tag: user.dumdum_look_radial
"""

# initialize
stop_job = None

# y axis based on power (volume)
neutral_power = 220
min_delta_y = 1
speed_scaler_y = .06

# x axis based on frequency
min_freq = 200
max_freq = 400
min_pitch = log(min_freq)
max_pitch = log(max_freq)
mid_pitch = (min_pitch + max_pitch) / 2

max_speed = 8
speed_scaler_x = max_speed / (max_pitch - mid_pitch)



@ctx.action_class('user')
class DumdumActions:
    def dumdum_start(ts:float, power:float, f0:float, f1:float, f2:float):
        """dumdum_start"""
        if stop_job:
            cron.cancel(stop_job)
            return

        ctrl.mouse_click(0, down=True)

    def dumdum_stop(ts:float, power:float, f0:float, f1:float, f2:float):
        """for debugging"""
        def do_stop():
            global stop_job
            ctrl.mouse_click(0,up=True)
            ctrl.mouse_click(0,up=True)
            stop_job = None
        global stop_job
        if stop_job:
            cron.cancel(stop_job)
        stop_job = cron.after("500ms", do_stop) 

    def dumdum_repeat(ts:float, power:float, f0:float, f1:float, f2:float): 
        """for debugging"""
        f = f0

        base_x = mid_pitch
        
        delta_x = (log(f) - base_x) * speed_scaler_x
        delta_y = (power - neutral_power) * speed_scaler_y
        
        delta_x, delta_y = map_radial(delta_y, delta_x)

        mouse_move(delta_x, -delta_y)
        actions.user.set_radial_indicator(True)
        actions.user.dumdum_widget(delta_x, -delta_y)
        #print("eee cont ", [int(x) for x in [10*ts, power, f0, f1, f2]])

def map_radial(r, θ):
    x = r * sin(θ)
    y = r * cos(θ)
    return x, y

should_print = True
def print_attributes_once(object):
    global should_print
    if should_print:
        should_print = False
        print([method_name for method_name in dir(object)
                  if callable(getattr(object, method_name))])

def mouse_move(dx, dy):
    import win32api, win32con
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,int(dx),int(dy),0,0)
    # with talon, but might not work in a game
    # mouse_pos = ctrl.mouse_pos()
    # x = mouse_pos[0] + delta*speed_scaler_x
    # y = mouse_pos[1]
    # ctrl.mouse_move(x, y)