from talon import Context, actions
ctx = Context()
ctx.matches = r"""
mode: user.gameboy
and win.title: /Crystal Caves HD/
"""

@ctx.action_class('user')
class UserActions:
    def noise_trigger_pop():
        actions.user.long_press('ctrl')

    def noise_hiss_start():
        # actions.user.long_press('alt')
        return

    def noise_hiss_stop():
        return

    def parrot_palate():
        actions.user.long_press('alt')
        return
        
