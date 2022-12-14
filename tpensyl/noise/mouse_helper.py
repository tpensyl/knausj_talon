import time

from talon import noise, ctrl
from talon import Module, Context

mod = Module()

#ctx = Context()
#ctx.matches = r"""
#os: windows
#"""

@mod.action_class
class TpensylClick:
    def slow_click():
        """Click with hold time"""
        ctrl.mouse_click(button=0, down=True)
        time.sleep(.016)
        ctrl.mouse_click(button=0, up=True)

    def game_click(button: int = 0, times: int = 1, hold: int = None):
        """Click with hold time"""
        wait = hold
        for i in range(times):
            ctrl.mouse_click(button, hold=hold, wait=wait)

    def toggle_drag(button: int = 0):
        """Toggle drag"""
        buttons_held_down = list(ctrl.mouse_buttons_down())
        if buttons_held_down:
            for button in buttons_held_down:
                ctrl.mouse_click(button=button, up=True)
            return
        else:
            ctrl.mouse_click(button=button, down=True)