from talon import Context, Module, actions, ctrl, cron
from time import time

mod = Module()

ctx = Context()
ctx.matches = r"""
mode: user.gameboy
and app.name: DSPGAME.exe
"""

last_rotate_time = time()
rotate_delta = .5

@ctx.action_class('user')
class UserActions:
    def parrot_palate():
        actions.key("shift:up")
        ctrl.mouse_click(1)

    def parrot_tut():
        actions.key("shift:up")
        actions.key("esc")

    def noise_hiss_start():
        ctrl.mouse_click(button=2, down=True)

    def noise_hiss_stop():
        ctrl.mouse_click(button=2, up=True)

    def whistle_action(delta):  
        actions.mouse_scroll(by_lines=False, y=delta)
        
        global last_rotate_time
        this_rotate_time = time()
        if this_rotate_time - last_rotate_time < rotate_delta:# and False :
            return
        else:
            actions.key("r")
            last_rotate_time = this_rotate_time

@mod.action_class
class Actions:
    def queue_click():
        "shift clicks to queue actions"
        actions.key("shift:down")
        ctrl.mouse_click(1)
        actions.sleep("15ms")
        actions.key("shift:up")
