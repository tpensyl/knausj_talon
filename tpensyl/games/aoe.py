from talon import Context, actions, ctrl
ctx = Context()
ctx.matches = r"""
app.name: Age of Empires: Definitive Edition
"""

@ctx.action_class('user')
class UserActions:
    def noise_pop():
        ctrl.mouse_click(1)

    def noise_hiss_start():
        ctrl.mouse_click(button=0, down=True)

    def noise_hiss_stop():
        ctrl.mouse_click(button=0, up=True)
