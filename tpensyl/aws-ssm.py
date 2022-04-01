from talon import Context, actions, Module

# TODO match on aws ssm?
# App definition
# mod = Module()
# mod.apps.gnome_terminal = """
# os: linux
# and app.exe: gnome-terminal-server
# os: linux
# and app.name: Gnome-terminal
# """

# # Context matching
# ctx = Context()
# ctx.matches = r"""
# app: gnome_terminal
# """


# global (overwrite linux/edit.py)
# @ctx.action_class('edit')
# class EditActions:
#     def page_down(): actions.key('shift-pagedown')
#     def page_up(): actions.key('shift-pageup')
#     def paste(): actions.key('ctrl-shift-v')
#     def copy(): actions.key('ctrl-shift-c')
#     def find(text: str = None):
#         actions.key('ctrl-shift-f')
#         if text:
#             actions.insert(text)
#     def delete_line():
#         actions.edit.line_start()
#         actions.key('ctrl-k')
#     # afaik not possible in gnome-terminal
#     def extend_left(): pass
#     def extend_right(): pass
#     def extend_up(): pass
#     def extend_down(): pass
#     def extend_word_left(): pass
#     def extend_word_right(): pass
