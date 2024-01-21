from talon import Context, actions, ctrl
ctx = Context()
ctx.matches = r"""
win.title: /Old Sins/
"""

@ctx.action_class('user')
class UserActions:
    def parrot_tut():
        actions.key('f23')

    def parrot_palate():
        ctrl.mouse_click(1)
