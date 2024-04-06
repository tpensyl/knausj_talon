from talon import Context, ctrl
ctx = Context()
ctx.matches = r"""
win.title: /Kittens Game.*/
"""

@ctx.action_class("user")
class UserActions:
    def parrot_palate():
        ctrl.mouse_click(0)
