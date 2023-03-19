from talon import Context, ctrl
ctx = Context()
ctx.matches = r"""
browser.host: lucid.app
"""

@ctx.action_class("user")
class UserActions:
    def noise_hiss_start():
        ctrl.mouse_click(1, down=True)

    def noise_hiss_stop():
        ctrl.mouse_click(1, up=True)
