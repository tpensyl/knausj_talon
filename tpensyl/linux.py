from talon import Context, ctrl, actions
ctx = Context()
ctx.matches = r"""
os: linux
"""

@ctx.action_class("user")
class UserActions:
    def whistle_action(delta:float):
        """Define action to take based on relative whistle pitch"""
        print(f'RAby_lines=False, y={delta}')
        #TODO make bylines configurable instead of overwriting
        actions.mouse_scroll(by_lines=True, y=delta)