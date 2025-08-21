from talon import Context, ctrl, actions
ctx = Context()
ctx.matches = r"""
mode: user.gameboy
os: windows
app.exe: sims.exe
"""

@ctx.action_class("user")
class UserActions:

    def pedal_center_down():
        actions.mouse_drag(1)

    def pedal_center_up():
        actions.mouse_release(1)

    def pedal_top_down():
        actions.key("shift-right")

    def pedal_right_down():
        actions.mouse_drag(0)

    def pedal_right_up():
        actions.mouse_release(0)

    def parrot_palate():
        ctrl.mouse_click(1)
