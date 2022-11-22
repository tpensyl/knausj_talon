from talon import Context, actions
ctx = Context()
ctx.matches = r"""
mode: user.gameboy
and win.title: /.*melonDS.*/
"""

@ctx.action_class('user')
class UserActions:
    def noise_pop():
        #actions.key('a')
        actions.key('a:down')
        actions.sleep('32ms')
        actions.key('a:up')
    def noise_hiss_start():
        actions.key('b:down')
        actions.key('p:down')
    def noise_hiss_stop():
        actions.key('b:up')
        actions.key('p:up')
