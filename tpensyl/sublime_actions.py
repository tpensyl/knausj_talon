from talon import Context, actions
ctx = Context()
ctx.matches = r"""
app: sublime
"""

@ctx.action_class('edit')
class EditActions:
    #TODO deprecated
    def indent_less():
        actions.key('ctrl-[')
    def indent_more():
        actions.key('ctrl-]')
