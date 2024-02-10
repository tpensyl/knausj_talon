from talon import Context, actions
ctx = Context()
ctx.matches = r"""
mode: user.gameboy
app.name: Sokobond.exe
"""

@ctx.action_class('user')
class UserActions:
    
    def noise_trigger_pop():
        actions.key('enter')
    
    def noise_hiss_start():
        actions.key('z:down')
    
    def noise_hiss_stop():
        actions.key('i:up')

    def parrot_tut():
        pass

    def parrot_palate():
        actions.key('z')
