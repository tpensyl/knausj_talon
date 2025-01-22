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
        print("parrot-scroll.py:palate triggered scroll down")
        actions.mouse_scroll(by_lines=True, y=5)

    # reusing continuous scroll does not work on linux, because it uses bylines equal false
    # def noise_hiss_start():
    #     print("#parrot-scroll.py:hiss triggered scroll up")
    #     actions.mouse_scroll(by_lines=True, y=-30)

    # def noise_hiss_stop():
    #     actions.mouse_scroll(by_lines=True, y=30)

    def noise_trigger_hiss(active):
        if active:
            actions.mouse_scroll(by_lines=True, y=-5)