from talon import Context, actions
ctx = Context()
ctx.matches = r"""
app.exe: /PCem98.exe/
"""

@ctx.action_class('user')
class UserActions:
    def noise_trigger_pop():
        actions.user.game_click(button=0, hold='50ms')

    # def noise_hiss_start():
    #     # actions.user.long_press('alt')
    #     return

    # def noise_hiss_stop():
    #     return

    def parrot_palate():
        actions.user.game_click(button=1, hold='50ms')
        
        
