from talon import Context, actions, ctrl
from time import time

ctx = Context()
ctx.matches = r"""
mode: user.gameboy
app.name: /RCT.EXE/
app.name: /.*OpenRCT2/
"""

LEFT_BUTTON = 0
RIGHT_BUTTON = 1

last_click_ts = time()
double_click_threshold = .3

@ctx.action_class('user')
class UserActions:
    def noise_trigger_pop():
        
        global last_click_ts
        new_click_ts = time()
        if new_click_ts - last_click_ts < double_click_threshold:
            ctrl.mouse_click(0, down=True)
        else:
            ctrl.mouse_click(0)
            last_click_ts = new_click_ts

    def noise_hiss_start():
        actions.user.mouse_drag(1)

    def noise_hiss_stop():
        ctrl.mouse_click(button=1, up=True)

    def parrot_palate():
        actions.key("esc")

    def parrot_tut():
        # actions.user.toggle_drag(0)  
        ctrl.mouse_click(1)
