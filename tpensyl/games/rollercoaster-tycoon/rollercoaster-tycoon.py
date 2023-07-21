from talon import Context, actions, ctrl

ctx = Context()
ctx.matches = r"""
mode: user.gameboy
app.name: /RCT.EXE/
"""

LEFT_BUTTON = 0
RIGHT_BUTTON = 1

@ctx.action_class('user')
class UserActions:
    def noise_trigger_pop():
        ctrl.mouse_click(0)

    def noise_hiss_start():
        actions.user.mouse_drag(1)

    def noise_hiss_stop():
        ctrl.mouse_click(button=1, up=True)

    def parrot_palate():
        actions.key("esc")

    def parrot_tut():
        actions.user.toggle_drag(0)  
