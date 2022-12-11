from talon import Context, actions, ctrl

ctx = Context()
ctx.matches = r"""
win.title: /Railroad Tycoon II.*/
"""

LEFT_BUTTON = 0
RIGHT_BUTTON = 1

@ctx.action_class('user')
class UserActions:
    def noise_pop():
        buttons_held_down = list(ctrl.mouse_buttons_down())
        if buttons_held_down:
            for button in buttons_held_down:
                ctrl.mouse_click(button=button, up=True)
            return
        
        actions.user.game_click(0, times=1, hold=16000)

    def noise_hiss_start():
        # safely cancel last drag for convenience
        actions.key('s')
        actions.key('t')
        actions.user.mouse_drag(0)

    def noise_hiss_stop():
        return
        #pop to stop drag
