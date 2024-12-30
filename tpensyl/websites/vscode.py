from talon import Context, ctrl, actions, ui
import sys

ctx = Context()
ctx.matches = r"""
app: vscode
"""

@ctx.action_class('user')
class Actions:
    def parrot_palate():
        return