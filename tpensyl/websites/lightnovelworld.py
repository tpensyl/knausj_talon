from talon import Context, actions
ctx = Context()
ctx.matches = r"""
win.title: /My Vampire System.*/
"""

@ctx.action_class("user")
class UserActions:
#     def parrot_palate():
#         actions.mouse_scroll(by_lines=True, y=15)

    def parrot_tut():
        actions.user.rango_click_element({
        "type": "primitive",
        "mark": {"type": "elementHint", "value": "ac"},
        })

#     def noise_hiss_start():
#         actions.user.mouse_scroll_up_continuous()

#     def noise_hiss_stop():
#         actions.user.mouse_scroll_stop()
