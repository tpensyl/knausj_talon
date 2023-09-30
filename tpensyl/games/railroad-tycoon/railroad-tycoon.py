from talon import Context, actions, ctrl

ctx = Context()
ctx.matches = r"""
mode: user.gameboy
win.title: /Railroad Tycoon II.*/
"""

LEFT_BUTTON = 0
RIGHT_BUTTON = 1

@ctx.action_class('user')
class UserActions:
    def noise_trigger_pop():
        buttons_held_down = list(ctrl.mouse_buttons_down())
        if buttons_held_down:
            for button in buttons_held_down:
                ctrl.mouse_click(button=button, up=True)
            return
        
        actions.user.game_click(0, times=1, hold=16000)

    def noise_hiss_start():
        actions.user.mouse_drag(1)

    def noise_hiss_stop():
        ctrl.mouse_click(button=1, up=True)

    def parrot_palate():
        actions.key("esc")

    def parrot_tut():
        actions.user.toggle_drag(0)  
