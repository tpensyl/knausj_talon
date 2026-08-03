from talon import Context, actions

ctx = Context()
ctx.matches = r"""
app: apple_terminal
and win.title: /[Cc]laude/
"""


@ctx.action_class("edit")
class EditActions:
    def line_insert_down():
        actions.key("end")
        actions.key("alt-enter")
