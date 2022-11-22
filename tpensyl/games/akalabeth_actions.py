from talon import Context, actions
ctx = Context()
ctx.matches = r"""
mode: user.gameboy
and win.title: /.*AKLABETH.*/
"""

@ctx.action_class('user')
class UserActions:
    def noise_pop():
        actions.key('up') 
        print("test tpensyl")
