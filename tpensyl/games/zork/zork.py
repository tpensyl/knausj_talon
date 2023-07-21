from talon import Context, actions
ctx = Context()
ctx.matches = r"""
win.title: /.*DOSBox.*ZORK.*/
"""

@ctx.action_class('user')
class UserActions:
    def noise_trigger_pop():
        actions.key('enter')
    def noise_hiss_start():
        actions.key('backspace:down')
    def noise_hiss_stop():
        actions.key('backspace:up')
