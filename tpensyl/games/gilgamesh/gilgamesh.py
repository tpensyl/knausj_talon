from talon import Context, actions, ctrl, cron
from time import time
ctx = Context()
ctx.matches = r"""
mode: user.gameboy
and win.title: SteamWorld Quest
"""

mouse_last_position = ctrl.mouse_pos()
mouse_last_sec = time() - 50

# Revert to mouse free action after this many seconds of mouse inactivity
MOUSE_MODE_TIMEOUT = 4

@ctx.action_class('user')
class UserActions:
    def noise_trigger_pop():
        # print("Gilgamesh pop click")
        # print((ctrl.mouse_pos() != mouse_last_position), (time() < mouse_last_sec + MOUSE_MODE_TIMEOUT))
        # print(time(), mouse_last_sec + MOUSE_MODE_TIMEOUT)
        global mouse_last_position, mouse_last_sec
        if((ctrl.mouse_pos() != mouse_last_position) 
           or (time() < mouse_last_sec + MOUSE_MODE_TIMEOUT)):
            actions.user.slow_click()
            mouse_last_position = ctrl.mouse_pos()
            mouse_last_sec = time()
        else:
            actions.key("enter")

        
    def parrot_palate():
            actions.key("esc") 