from talon import Module, Context, actions

mod = Module()
ctx = Context()

mod.apps.shapez = r"""
os: windows
and app.exe: /^shapezio\.exe$/i
"""

ctx.matches = r"""
os: windows
app: shapez
"""

# @mod.action_class
# class Actions:
