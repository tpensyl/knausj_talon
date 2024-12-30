from talon import Context, Module, actions

mod = Module()
mod.tag("parrot_scroll", desc="change parrot noises to scroll")

ctx = Context()
ctx.matches = """
tag: user.parrot_scroll
"""

@ctx.action_class("user")
class UserActions:
    def parrot_palate():
        actions.mouse_scroll(by_lines=True, y=15)

    def noise_hiss_start():
        actions.user.mouse_scroll_up_continuous()

    def noise_hiss_stop():
        actions.user.mouse_scroll_stop()