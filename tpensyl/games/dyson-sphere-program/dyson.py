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
right_click_action = actions.user.move_command
set_move_mode_cron = None
@ctx.action_class('user')
class UserActions:
    def parrot_palate():
        right_click_action()

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

    def add_mode():
        "temporarily make right clicks into queuing mode"
        global right_click_action
        global set_move_mode_cron
        if set_move_mode_cron:
            cron.cancel(set_move_mode_cron)
            set_move_mode_cron = None
        right_click_action = actions.user.queue_click
        set_move_mode_cron = cron.after("20s", set_move_mode)

    def move_command():
        "move the mech"
        actions.key("shift:up")
        ctrl.mouse_click(1)

def set_move_mode():
    global right_click_action
    right_click_action = actions.user.move_command