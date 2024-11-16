from talon import Context, ctrl

ctx = Context()
ctx.matches = r"""
app: vscode
"""

@ctx.action_class("user")
class UserActions:
    def noise_hiss_start():
        return
    
    def noise_hiss_stop():
        return
