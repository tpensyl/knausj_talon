from talon import Context, ctrl, actions, ui
import sys

# sys.path.append('../../plugin/draft_editor/')
sys.path.append('C:/Users/Tommy/AppData/Roaming/talon/user/knausj_talon/plugin/draft_editor')
import draft_editor

ctx = Context()
ctx.matches = r"""
title: /.*Online LaTeX Editor Overleaf/
"""

# # hack... - In chrome on windows it seems when returning focus to overleaf, SOMETIMES it removes the selection.
# UPDATE: this is not specific to overleaf, but any chrome if vscode is maximized!
# @ctx.action_class('user')
# class Actions:
#     def draft_editor_open_pre_switch_hook():
#         actions.edit.cut()

@ctx.action_class('user')
class NoiseActions:
    def parrot_palate():
        """parrot palate sound, has some false positives with speech"""
        # actions.key("ctrl:down")
        ctrl.mouse_click(0)
        # actions.key("ctrl:up")
        pass