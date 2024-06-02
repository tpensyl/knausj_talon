from talon import Context, actions
ctx = Context()
ctx.matches = r"""
os: windows
app.exe: Mathematica.exe
"""

# @ctx.action_class('edit')
# class EditActions:
#     def dummy_function():
#         x=3