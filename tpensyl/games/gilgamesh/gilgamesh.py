from talon import Context, actions
ctx = Context()
ctx.matches = r"""
mode: user.gameboy
and win.title: SteamWorld Quest
"""

@ctx.action_class('user')
class UserActions:
    # def noise_trigger_pop():
    #     actions.key('up')
        
    def parrot_palate():
            actions.key("esc") 