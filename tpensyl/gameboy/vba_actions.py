from talon import Context, actions
ctx = Context()
ctx.matches = r"""
mode: user.gameboy
and win.title: /.*VisualBoyAdvance.*/
"""

@ctx.action_class('user')
class UserActions:
    def noise_pop():
        actions.key('l:down')
        actions.sleep('32ms')
        actions.key('l:up')
    def noise_hiss_start():
        actions.key('r:down')
        actions.key('t')
    def noise_hiss_stop():
        actions.key('r:up')
        actions.key('t')
