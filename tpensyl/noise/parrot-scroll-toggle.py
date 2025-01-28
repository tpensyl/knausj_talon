from talon import Context, Module, actions

mod = Module()
ctx = Context()
ctx.tags = ["user.parrot_scroll"]

@mod.action_class
class UserActions2:
    def set_parrot_scroll_mode(enabled: bool):
        """ Enable parent scroll mode """
        ctx.tags = ["user.parrot_scroll"] if enabled else []