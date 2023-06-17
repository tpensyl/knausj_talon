from talon import Context, actions
ctx = Context()
ctx.matches = r"""
mode: user.gameboy
and win.title: /.*BStone.*/
"""

@ctx.action_class('user')
class UserActions:
    def parrot_tut():
        actions.key('f23')

    def parrot_palate():
        actions.key('space')
