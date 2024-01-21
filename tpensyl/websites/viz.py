from talon import Context, ctrl, actions
ctx = Context()
ctx.matches = r"""
os: windows
and app.exe: chrome.exe
and win.title: /VIZ.*/
"""

@ctx.action_class("user")
class UserActions:
    def parrot_palate():
        actions.key("left")

    def parrot_tut():
        actions.key("right")