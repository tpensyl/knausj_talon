from talon import Context, actions, ctrl
ctx = Context()
ctx.matches = r"""
mode: user.gameboy
win.title: /FTL: Faster Than Light/
"""

@ctx.action_class('user')
class UserActions:
    def noise_pop():
        ctrl.mouse_click(0)
    def noise_hiss_start():
        ctrl.mouse_click(1)
    def noise_hiss_stop():
        return
