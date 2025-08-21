from talon import Context, ctrl, actions
ctx = Context()
ctx.matches = r"""
mode: user.gameboy
os: windows
app.name: RuneScape Client
"""

@ctx.action_class("user")
class UserActions:

    def noise_trigger_pop():
        actions.user.game_click(button=0, hold='50ms')

    def noise_trigger_hiss(active):
        if active:
            actions.mouse_drag(2)
        else:
            actions.mouse_release(2)

    def pedal_center_down():
        actions.mouse_drag(2)

    def pedal_center_up():
        actions.mouse_release(2)

    def pedal_top_down():
        actions.mouse_drag(0)

    def pedal_top_up():
        actions.mouse_release(0)

    def pedal_right_down():
        actions.user.game_click(button=1, hold='50ms')

    def pedal_right_up():
        pass

    def pedal_left_down():
        actions.user.game_click(button=0, hold='50ms')

    def pedal_left_up():
        # actions.mouse_release(0)
        pass

    def parrot_palate():
        actions.key("space")
        # ctrl.mouse_click(1)

    def parrot_tut():
        ctrl.mouse_click(1)
