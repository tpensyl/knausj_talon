from talon import Context, Module, actions

ctx = Context()

ctx = Context()
ctx.matches = r"""
mode: command
and app.name: Satisfactory
"""

@ctx.action_class("edit")
class EditActions:
    def line_insert_down():
        # end+enter on a blank line in multiline text boxes crashes the game
        #actions.edit.line_end()
        actions.key("right:100")
        actions.key("shift-enter")
