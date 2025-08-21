from talon import Context, ctrl, actions
ctx = Context()
ctx.matches = r"""
win.title: /Kittens Game.*/
"""

@ctx.action_class("user")
class UserActions:
    def pedal_right_down():
        actions.key("ctrl:down")
        ctrl.mouse_click(0)
        actions.key("ctrl:up")

    def pedal_center_down():
        actions.user.mouse_auto_click(250)
