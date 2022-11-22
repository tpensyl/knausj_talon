from talon import Context, actions
ctx = Context()
ctx.matches = r"""
mode: user.gameboy
and win.title: /Crystal Caves HD/
"""

@ctx.action_class('user')
class UserActions:
    def noise_pop():
        actions.key('j')
    def noise_hiss_start():
        actions.key('f')
    def noise_hiss_stop():
        return
