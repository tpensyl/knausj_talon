from talon import Context, actions, ctrl

ctx = Context()
ctx.matches = r"""
win.title: /DOSBox.*KRONDOR*/
"""
@ctx.action_class('user')
class UserActions:
    def noise_pop():
        #actions.user.slow_click()
        actions.user.game_click(0, times=1, hold=16000)

    def noise_hiss_start():
        actions.user.mouse_drag(0)

    def noise_hiss_stop():
        # actions.user.mouse_drag_end()
        actions.user.slow_click()
